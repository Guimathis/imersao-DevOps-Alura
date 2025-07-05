# Imersão DevOps - Alura Google Cloud

Este projeto é uma API desenvolvida com FastAPI para gerenciar alunos, cursos e matrículas em uma instituição de ensino.

## Pré-requisitos

- [Python 3.10 ou superior instalado](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/get-started/)

## Passos para subir o projeto

1. **Faça o download do repositório:**
   [Clique aqui para realizar o download](https://github.com/guilhermeonrails/imersao-devops/archive/refs/heads/main.zip)

2. **Crie um ambiente virtual:**
   ```sh
   python3 -m venv ./venv
   ```

3. **Ative o ambiente virtual:**
   - No Linux/Mac:
     ```sh
     source venv/bin/activate
     ```
   - No Windows, abra um terminal no modo administrador e execute o comando:
   ```sh
   Set-ExecutionPolicy RemoteSigned
   ```

     ```sh
     venv\Scripts\activate
     ```

4. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

5. **Execute a aplicação:**
   ```sh
   uvicorn app:app --reload
   ```

6. **Acesse a documentação interativa:**

   Abra o navegador e acesse:  
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

   Aqui você pode testar todos os endpoints da API de forma interativa.

---

## Passos para subir o projeto com Docker

1. **Construa e suba os contêineres:**
   Na raiz do projeto, execute o seguinte comando:
   ```sh
   docker-compose up --build
   ```

2. **Acesse a documentação interativa:**

   Abra o navegador e acesse:  
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

   Aqui você pode testar todos os endpoints da API de forma interativa.
---


---

## Fazendo Deploy ou Atualizando no Google Cloud

1.  **Autentique-se e configure o projeto (se for a primeira vez):**
    ```sh
    gcloud auth login
    gcloud config set project SEU_PROJECT_ID
    ```

2.  **Execute o comando de deploy para criar ou atualizar o serviço:**
    Este comando irá construir a imagem do seu container a partir do código-fonte local, enviá-la para o Artifact Registry e fazer o deploy de uma nova revisão do seu serviço no Cloud Run.

    ```sh
    gcloud run deploy api-escola --source . --port 8000 --region southamerica-east1 --allow-unauthenticated
    ```
    - **`api-gestao-escolar`**: Substitua pelo nome do seu serviço. Use o mesmo nome para atualizar.
    - **`--source .`**: Indica que o código-fonte para o build está no diretório atual.
    - **`--port 8000`**: Expõe a porta 8000 do container, que é a porta que o Uvicorn usa.
    - **`--region sua-regiao`**: Especifique a região do deploy (ex: `us-central1`).
    - **`--allow-unauthenticated`**: Permite que a API seja acessada publicamente. Remova se a sua API precisar de autenticação.


## Estrutura do Projeto



## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação FastAPI.
- `models.py`: Modelos do banco de dados (SQLAlchemy).
- `schemas.py`: Schemas de validação (Pydantic).
- `database.py`: Configuração do banco de dados SQLite.
- `routers/`: Diretório com os arquivos de rotas (alunos, cursos, matrículas).
- `requirements.txt`: Lista de dependências do projeto.

---

- O banco de dados SQLite será criado automaticamente como `escola.db` na primeira execução.
- Para reiniciar o banco, basta apagar o arquivo `escola.db` (isso apagará todos os dados).

---
