
# Assistente Virtual Felipe — Documentação do Projeto
## 🧩 Descrição

O **Assistente Virtual Felipe** é um sistema inteligente integrado a agentes de IA e serviços externos, projetado para interagir com usuários de forma dinâmica e personalizada.
O projeto combina **Django**, **Docker**, **n8n** e integrações com **Evolution API**, **Redis**, **SUAP** e **LLMs (OpenAI e Google Cloud)**, permitindo comunicações automatizadas, como via **WhatsApp**.

## 🚀 Configuração do Ambiente

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/rafinhasdev/Assistente-Virtual.git
cd Assistente-Virtual
```

### 2️⃣ Criar e ativar o ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Aplicar as migrações do banco de dados

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🐳 Executando com Docker

### 1️⃣ Construir e subir os containers

```bash
docker-compose up -d
```

### 2️⃣ Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto e adicione as chaves necessárias, incluindo sua **API Key do SUAP**:

```env
SUAP_API_KEY=
```

Documentação da API do SUAP:
👉 [https://suap.com.br/api/](https://suap.com.br/api/)

---

## 🔗 Integração com o n8n

### 1️⃣ Conectar o WhatsApp via Evolution API

Acesse o painel de gerenciamento do Evolution API:

```bash
http://evolutionapi.host.internal.docker/manage
```

### 2️⃣ Conectar os **Evolution Nodes** no fluxo do n8n

```bash
evolution-api-nodes
```

### 3️⃣ Integrar credenciais de **Redis** e **LLMs**

Configurações típicas utilizadas no projeto:

* **Redis**:

  ```bash
  http://redis.host.internal.docker
  ```

* **Google Cloud (para LLMs ou serviços adicionais)**:
  👉 [https://cloud.google.com/](https://cloud.google.com/)

* **OpenAI API (para integração com GPTs)**:
  👉 [https://platform.openai.com/](https://platform.openai.com/)

---

## 🧠 Tecnologias Utilizadas

| Categoria                | Ferramenta / Tecnologia           |
| ------------------------ | --------------------------------- |
| Backend                  | Django 5.2, Django REST Framework |
| Infraestrutura           | Docker, Docker Compose            |
| Banco de Dados           | PostgreSQL                        |
| Automação e Fluxos       | n8n                               |
| Comunicação              | Evolution API (WhatsApp)          |
| Cache e Mensageria       | Redis                             |
| IA e LLMs                | OpenAI, Google Cloud              |
| Integração Institucional | SUAP API                          |

---

## 📊 Arquitetura do Sistema

```mermaid
flowchart TD
    A[Usuário via WhatsApp 📱] --> B[Evolution API 🔄]
    B --> C[n8n ⚙️ Workflow]
    C --> D[Django Backend 🧠]
    D --> E[(PostgreSQL 🗄️)]
    D --> F[Redis ⚡ Cache]
    C --> G[OpenAI / Google Cloud 🤖]
    D --> H[SUAP API 🏫]

    subgraph
        B
        C
        D
        F
        E
    end
```

**Fluxo Resumido:**

1. O usuário envia uma mensagem via **WhatsApp**.
2. A **Evolution API** recebe e encaminha a mensagem para o **n8n**.
3. O **n8n** processa o fluxo e se comunica com o **Django Backend** e com as **LLMs** (OpenAI/Google).
4. O Django acessa o **PostgreSQL** e **Redis**, além de autenticar usuários via **SUAP API**.
5. A resposta é enviada de volta ao WhatsApp.

---

## 📂 Estrutura do Projeto (Resumo)

```
Assistente-Virtual/
├── accounts/              # Autenticação e usuários
├── dashboard/             # Interface principal
├── core/                  # Configurações Django
├── app/                   # Integrações com n8n e Evolution
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── manage.py
```

## 💬 Contato

Desenvolvido por **Rafael (rafinhasdev)**
📧 [rafaelnunes.prof@gmail.com](mailto:rafaelnunes.prof@gmail.com)
🔗 [GitHub - rafinhasdev](https://github.com/rafinhasdev)
