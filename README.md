# ZapSign Agents OpenAI

Este projeto implementa um agente de IA para criação e envio de documentos para assinatura utilizando a API da ZapSign e a OpenAI.

## Descrição

O ZapSign Agents OpenAI é um assistente que ajuda na criação de documentos legais e no envio para assinatura digital. O sistema utiliza agentes de IA da OpenAI (https://platform.openai.com/docs/guides/agents-sdk) para:

- Conversar com o usuário e coletar informações sobre o documento
- Gerar documentos e contratos em formato markdown
- Enviar os documentos para assinatura através da API da ZapSign

## Pré-requisitos

- Python 3.8 ou superior
- Conta na OpenAI com acesso à API
- Conta na ZapSign com acesso à API

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/renatohr/zapsign-agent-openai
   ```

2. Crie e ative um ambiente virtual:

   - No Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

   - No Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto com as seguintes informações:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ZAPSIGN_API_KEY=your_zapsign_api_key
     ```

## Como executar

1. Com o ambiente virtual ativado, execute o script principal:
   ```bash
   python zapsign_agent.py
   ```

2. Siga as instruções do assistente no terminal:
   - Informe o tipo de documento que deseja criar
   - Forneça o contexto e informações relevantes para o documento
   - Informe os nomes e emails dos signatários
   - Revise o documento gerado
   - Confirme o envio para assinatura

3. Você pode acompanhar os Traces (logs de execução do seu agente) via Dashboard da OpenAI:
    - https://platform.openai.com/traces

## Estrutura do projeto

- `zapsign_agent.py`: Arquivo principal contendo a lógica dos agentes e a integração com as APIs
- `requirements.txt`: Lista de dependências do projeto
- `.env`: Arquivo de configuração com as chaves de API

## Observações importantes

- Nunca compartilhe suas chaves de API em repositórios públicos
- As chaves de API no arquivo `.env` de exemplo são fictícias e devem ser substituídas pelas suas próprias chaves
- O projeto utiliza a biblioteca `openai-agents` que está em desenvolvimento, então podem ocorrer mudanças na API

## Solução de problemas

- Verifique se:
  - As chaves de API estão corretas no arquivo `.env`
  - Todas as dependências foram instaladas corretamente
  - Você está usando uma versão compatível do Python

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Exemplo de uso
<pre>
(venv) PS C:\zapsign-agents-openai> python .\zapsign_agent.py

System: Olá! Sou o assistente de criação de documentos e envio para assinatura. Para começar, por favor, diga o tipo de documento que você deseja criar.

User: oi, quero criar um contrato de prestação de serviço de software

System: Ótimo! Vamos criar um contrato de prestação de serviço de software. Para isso, preciso de algumas informações:

1. **Descrição do serviço**: Que tipo de serviço de software será prestado?
2. **Preço**: Qual será o valor cobrado pelo serviço?
3. **Prazos**: Qual é o prazo de início e término do serviço?
4. **Formas de pagamento**: Como será feito o pagamento?
5. **Obrigações das partes**: Quais são as responsabilidades de cada parte envolvida?
6. **Nome e email do prestador de serviço**:
7. **Nome e email do cliente**:

Por favor, me forneça essas informações para que eu possa prosseguir.

User: criação de agentes de ia por R$1mil, em 30 dias. 50% no inicio e 50% no fim. Obrigações padrão. prestador sou eu (renato haidamous renato@zapsign.com.br) e cliente é a empresa XPTO (xpto@xpto.com.br)

System: # Contrato de Prestação de Serviço de Software

**Entre as partes:**

**Prestador de Serviço:**
- Nome: Renato Haidamous
- Email: renato@zapsign.com.br

**Cliente:**
- Nome: Empresa XPTO
- Email: xpto@xpto.com.br

**As partes acima identificadas têm entre si justo e contratado o seguinte, que mutuamente aceitam, a saber:**

## 1. Descrição do Serviço

O Prestador de Serviço se compromete a prestar serviços de criação de agentes de inteligência artificial para a Cliente.

## 2. Preço

O preço total pelos serviços prestados será de R$ 1.000,00 (mil reais).

## 3. Prazos

O serviço será iniciado imediatamente após a assinatura deste contrato e deverá ser concluído no prazo de 30 (trinta) dias.

## 4. Formas de Pagamento

O pagamento será realizado da seguinte forma:
- 50% no início do serviço.
- 50% na conclusão do serviço.

## 5. Obrigações das Partes

### 5.1. Obrigações do Prestador de Serviço

- Prestar o serviço conforme descrito.
- Manter sigilo sobre as informações confidenciais fornecidas pela Cliente.

### 5.2. Obrigações do Cliente

- Fornecer todas as informações necessárias para a execução do serviço.
- Efetuar os pagamentos conforme estipulado no contrato.

## 6. Confidencialidade

As partes concordam em manter a confidencialidade de quaisquer dados ou informações fornecidas e reconhecem que essas informações são de propriedade exclusiva da parte divulgadora.

## 7. Rescisão

O contrato poderá ser rescindido por ambas as partes mediante aviso prévio de 15 (quinze) dias, sem prejuízo das cobranças proporcionalmente devidas ao período de vigência do contrato.

## 8. Foro

Fica eleito o foro da comarca de São Paulo, Estado de São Paulo, para dirimir quaisquer dúvidas oriundas do presente contrato.

---

Renato, deseja editar ou adicionar alguma informação ao contrato?

User: quero mudar o foro para Belo Horizonte, MG. e data de assinatura pode colocar data de hoje

System: # Contrato de Prestação de Serviço de Software

**Entre as partes:**

**Prestador de Serviço:**
- Nome: Renato Haidamous
- Email: renato@zapsign.com.br

**Cliente:**
- Nome: Empresa XPTO
- Email: xpto@xpto.com.br

**As partes acima identificadas têm entre si justo e contratado o seguinte, que mutuamente aceitam, a saber:**

## 1. Descrição do Serviço

O Prestador de Serviço se compromete a prestar serviços de criação de agentes de inteligência artificial para a Cliente.

## 2. Preço

O preço total pelos serviços prestados será de R$ 1.000,00 (mil reais).

## 3. Prazos

O serviço será iniciado imediatamente após a assinatura deste contrato e deverá ser concluído no prazo de 30 (trinta) dias.

## 4. Formas de Pagamento

O pagamento será realizado da seguinte forma:
- 50% no início do serviço.
- 50% na conclusão do serviço.

## 5. Obrigações das Partes

### 5.1. Obrigações do Prestador de Serviço

- Prestar o serviço conforme descrito.
- Manter sigilo sobre as informações confidenciais fornecidas pela Cliente.

### 5.2. Obrigações do Cliente

- Fornecer todas as informações necessárias para a execução do serviço.
- Efetuar os pagamentos conforme estipulado no contrato.

## 6. Confidencialidade

As partes concordam em manter a confidencialidade de quaisquer dados ou informações fornecidas e reconhecem que essas informações são de propriedade exclusiva da parte divulgadora.

## 7. Rescisão

O contrato poderá ser rescindido por ambas as partes mediante aviso prévio de 15 (quinze) dias, sem prejuízo das cobranças proporcionalmente devidas ao período de vigência do contrato.

As partes concordam em manter a confidencialidade de quaisquer dados ou informações fornecidas e reconhecem que essas informações são de propriedade exclusiva da parte divulgadora.

## 8. Foro

Fica eleito o foro da comarca de Belo Horizonte, Estado de Minas Gerais, para dirimir quaisquer dúvidas oriundas do presente contrato.

## 9. Data de Assinatura

Este contrato é assinado em 14 de março de 2025.

---

Deseja mais alguma alteração ou está tudo certo?

User: tudo certo! pode enviar pra assinatura por favor

System: O contrato foi enviado para assinatura com sucesso. Aqui estão os links para assinar:

- **Renato Haidamous**: [Assinar Contrato](https://app.zapsign.com.br/verificar/ecd6a489-1b99-44e6-825e-cc70a21b8a05)
- **Empresa XPTO**: [Assinar Contrato](https://app.zapsign.com.br/verificar/a9aa3c96-3333-4348-bf89-3d1f916ebc8a)

Por favor, acesse os links para completar as assinaturas. Se precisar de mais alguma coisa, estou à disposição!
</pre>
