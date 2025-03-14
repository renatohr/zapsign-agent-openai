# ZapSign Agents OpenAI

This project implements an AI agent for creating and sending documents for signature using the ZapSign API and OpenAI.

## Description

The ZapSign Agents OpenAI is an assistant that helps in creating legal documents and sending them for digital signature. The system uses OpenAI agents (https://platform.openai.com/docs/guides/agents-sdk) to:

- Converse with the user and collect information about the document
- Generate documents and contracts in markdown format
- Send the documents for signature through the ZapSign API

## Prerequisites

- Python 3.8 or higher
- An OpenAI account with API access
- A ZapSign account with API access

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/renatohr/zapsign-agent-openai
   ```

2. Create and activate a virtual environment:

   - On Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

   - On Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the environment variables:
   - Create a `.env` file at the root of the project with the following information:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ZAPSIGN_API_KEY=your_zapsign_api_key
     ```

## How to Run

1. With the virtual environment activated, run the main script:
   ```bash
   python zapsign_agent.py
   ```

2. Follow the assistant's instructions in the terminal:
   - Specify the type of document you want to create
   - Provide context and relevant information for the document
   - Provide the names and emails of the signatories
   - Review the generated document
   - Confirm sending for signature

3. You can track the Traces (execution logs of your agent) via the OpenAI Dashboard:
    - https://platform.openai.com/traces

## Project Structure

- `zapsign_agent.py`: Main file containing the logic of the agents and integration with the APIs
- `requirements.txt`: List of project dependencies
- `.env`: Configuration file with API keys

## Important Notes

- Never share your API keys in public repositories
- The API keys in the example `.env` file are fictitious and should be replaced with your own keys
- The project uses the `openai-agents` library which is under development, so API changes may occur

## Troubleshooting

- Check if:
  - The API keys are correct in the `.env` file
  - All dependencies were installed correctly
  - You are using a compatible version of Python

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.

## Usage Example
<pre>
(venv) PS C:\zapsign-agents-openai> python .\zapsign_agent.py

System: Hello! I am the document creation and signature sending assistant. To start, please tell me the type of document you want to create.

User: hi, I want to create a software service contract

System: Great! Let's create a software service contract. For that, I need some information:

1. **Service Description**: What type of software service will be provided?
2. **Price**: What will be the charge for the service?
3. **Deadlines**: What is the start and end date of the service?
4. **Payment Methods**: How will the payment be made?
5. **Obligations of the parties**: What are the responsibilities of each party involved?
6. **Name and email of the service provider**:
7. **Name and email of the client**:

Please provide me with this information so I can proceed.

User: creation of AI agents for R$1,000, in 30 days. 50% at the start and 50% at the end. Standard obligations. I am the provider (Renato Haidamous renato@zapsign.com.br) and the client is company XPTO (xpto@xpto.com.br)

System: # Software Service Contract

**Between the parties:**

**Service Provider:**
- Name: Renato Haidamous
- Email: renato@zapsign.com.br

**Client:**
- Name: Company XPTO
- Email: xpto@xpto.com.br

**The parties identified above have agreed and contracted the following, which they mutually accept, as follows:**

## 1. Service Description

The Service Provider agrees to provide AI agent creation services to the Client.

## 2. Price

The total price for the services provided will be R$ 1,000.00 (one thousand reais).

## 3. Deadlines

The service will start immediately after the signing of this contract and must be completed within 30 (thirty) days.

## 4. Payment Methods

Payment will be made as follows:
- 50% at the start of the service.
- 50% upon completion of the service.

## 5. Obligations of the Parties

### 5.1. Obligations of the Service Provider

- Provide the service as described.
- Maintain confidentiality of the confidential information provided by the Client.

### 5.2. Obligations of the Client

- Provide all necessary information for the execution of the service.
- Make payments as stipulated in the contract.

## 6. Confidentiality

The parties agree to maintain the confidentiality of any data or information provided and acknowledge that this information is the exclusive property of the disclosing party.

## 7. Termination

The contract may be terminated by both parties with 15 (fifteen) days' notice, without prejudice to the charges proportionally due for the contract term.

## 8. Jurisdiction

The jurisdiction of the district of São Paulo, State of São Paulo, is elected to resolve any doubts arising from this contract.

---

Renato, would you like to edit or add any information to the contract?

User: I want to change the jurisdiction to Belo Horizonte, MG. and the signing date can be today's date

System: # Software Service Contract

**Between the parties:**

**Service Provider:**
- Name: Renato Haidamous
- Email: renato@zapsign.com.br

**Client:**
- Name: Company XPTO
- Email: xpto@xpto.com.br

**The parties identified above have agreed and contracted the following, which they mutually accept, as follows:**

## 1. Service Description

The Service Provider agrees to provide AI agent creation services to the Client.

## 2. Price

The total price for the services provided will be R$ 1,000.00 (one thousand reais).

## 3. Deadlines

The service will start immediately after the signing of this contract and must be completed within 30 (thirty) days.

## 4. Payment Methods

Payment will be made as follows:
- 50% at the start of the service.
- 50% upon completion of the service.

## 5. Obligations of the Parties

### 5.1. Obligations of the Service Provider

- Provide the service as described.
- Maintain confidentiality of the confidential information provided by the Client.

### 5.2. Obligations of the Client

- Provide all necessary information for the execution of the service.
- Make payments as stipulated in the contract.

## 6. Confidentiality

The parties agree to maintain the confidentiality of any data or information provided and acknowledge that this information is the exclusive property of the disclosing party.

## 7. Termination

The contract may be terminated by both parties with 15 (fifteen) days' notice, without prejudice to the charges proportionally due for the contract term.

The parties agree to maintain the confidentiality of any data or information provided and acknowledge that this information is the exclusive property of the disclosing party.

## 8. Jurisdiction

The jurisdiction of the district of Belo Horizonte, State of Minas Gerais, is elected to resolve any doubts arising from this contract.

## 9. Signing Date

This contract is signed on March 14, 2025.

---

Would you like any more changes or is everything okay?

User: everything is fine! please send it for signature

System: The contract has been successfully sent for signature. Here are the links to sign:

- **Renato Haidamous**: [Sign Contract](https://app.zapsign.com.br/verificar/ecd6a489-1b99-44e6-825e-cc70a21b8a05)
- **Company XPTO**: [Sign Contract](https://app.zapsign.com.br/verificar/a9aa3c96-3333-4348-bf89-3d1f916ebc8a)

Please access the links to complete the signatures. If you need anything else, I'm at your disposal!
</pre>
