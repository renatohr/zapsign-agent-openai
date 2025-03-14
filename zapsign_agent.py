import os
import asyncio
import requests
import json
from dotenv import load_dotenv
from datetime import datetime
from pydantic import BaseModel
from typing import List, Dict, Any

from agents import Agent, Runner, function_tool, set_tracing_export_api_key, handoff


# change the default language of the assistant if you want
language = "portuguese"


load_dotenv()
set_tracing_export_api_key(os.getenv("OPENAI_API_KEY"))


# Data models
class SignerInfo(BaseModel):
    name: str
    email: str

class DocumentContext(BaseModel):
    document_type: str
    context: Dict[str, Any]
    document_name: str
    signers: List[SignerInfo]

class SigningResult(BaseModel):
    document: str
    signature_details: Dict[str, Any]


@function_tool
def get_today_date() -> str:
    return datetime.now().strftime("%d/%m/%Y")

@function_tool
def send_for_signature(document_name: str, markdown_text: str, signers: List[SignerInfo]) -> Dict[str, Any]:
    base_url = "https://api.zapsign.com.br/api/v1"
    headers = {
        "Authorization": f"Bearer {os.getenv('ZAPSIGN_API_TOKEN')}",
        "Content-Type": "application/json"
    }
    
    signers_data = [{"name": signer.name, "email": signer.email} for signer in signers]
    
    payload = {
        "name": document_name,
        "markdown_text": markdown_text,
        "signers": signers_data,
        "lang": "pt-br"
    }
    
    response = requests.post(
        f"{base_url}/docs",
        headers=headers,
        json=payload
    )
    
    if response.status_code != 200:
        raise Exception(f"Error sending document: {response.text}")
        
    return response.json()


conversation_agent = Agent(
    name="conversation_agent",
    instructions="""
    You are a legal expert that handles conversation with the user to understand what type of document the person wants to create, 
    asks relevant questions of this type of document (e.g. if a service contract, ask for the service description and price, if a promissory note, ask for the amount, interest rate, etc.), 
    and also asks for the signers name and email.
    While the user has not provided all the information, you should ask for it.
    """,
    tools=[get_today_date]
)

document_agent = Agent(
    name="document_agent",
    instructions="""
    You are a legal document expert that creates professional documents in markdown format.
    Generate a legal document based on context provided by the user.
    Please format the document in markdown, including all necessary legal clauses and formatting. Answer in {language} (or the language the user wants) and ask if the user wants to edit or add any information.
    """,
    tools=[get_today_date]
)

signing_agent = Agent(
    name="signing_agent",
    instructions="""
    You are an assistant that sends documents for signature using ZapSign API.
    You will receive a document in markdown format and a list of signers.
    You will send the document for signature using the ZapSign API (send_for_signature tool).
    """,
    tools=[send_for_signature]
)

coordinator_agent = Agent(
    name="coordinator_agent",
    instructions="""
    You coordinate document generation and signing process. 
    If the user has not provided all the information needed to generate the document, handoff to the conversation_agent and end there.
    Only handoff to the document_agent if the user has provided all the information needed to generate the document.
    Only handoff to the signing_agent if the document_agent has generated the document and the user has confirmed the document and signers names and emails.
    """,
    handoffs=[handoff(conversation_agent), handoff(document_agent), handoff(signing_agent)],
)


async def main():
    interactions = []
    if language == "portuguese":
        print('System: Olá! Sou o assistente de criação de documentos e envio para assinatura. Para começar, por favor, diga o tipo de documento que você deseja criar.\n')
    else:
        print('System: Hello! I am the document creation and signature sending assistant. To start, please tell me the type of document you want to create.\n')
    while True:
        user_input = input('User: ')
        user_input_line = 'User: ' + user_input
        interactions.append(user_input_line)

        interactions_str = '\n'.join(interactions)
        print('\n...', end='\r')
        result = await Runner.run(coordinator_agent, input=interactions_str)

        result_line = 'System: ' + result.final_output
        interactions.append(result_line)
        print(f"{result_line}\n")

if __name__ == "__main__":
    # Fix for the "Event loop is closed" error on Windows
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())