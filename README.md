# Resumo do Projeto ClarkeEnergia

## Visão Geral
O ClarkeEnergia é um sistema desenvolvido para gerenciar fornecedores de energia e o consumo dos usuários. O projeto é dividido em duas partes principais:
- **Backend**: Responsável pelo processamento de dados e regras de negócio.
- **Frontend**: Interface interativa para visualização e interação com o sistema.

Cada parte do sistema possui um README específico:
1. **README Geral** (este arquivo): Explica a estrutura do projeto como um todo.
2. **README Backend**: Contém detalhes técnicos e instruções de instalação da API desenvolvida em Flask.
3. **README Frontend**: Explica o funcionamento do sistema React.js, responsável pela interface do usuário.

## Tecnologias Utilizadas
O projeto utiliza tecnologias modernas para garantir escalabilidade, eficiência e uma boa experiência do usuário:

### **Backend**
- **Linguagem**: Python
- **Framework**: Flask
- **Banco de Dados**: PostgreSQL/SQLite
- **ORM**: SQLAlchemy
- **Migrações**: Alembic
- **Testes**: Pytest

> **Nota:** O banco de dados utilizado depende da variável `MODE_DEBUG` no arquivo `.env` do backend:
> - Se `MODE_DEBUG=True`, o banco de dados SQLite será utilizado, ideal para testes automatizados.
> - Se `MODE_DEBUG=False`, o PostgreSQL será utilizado para ambiente de produção.

#### Exemplo de `.env` do Backend:
```ini
DATABASE_HOST=localhost
DATABASE_USER=postgres
DATABASE_PASSWORD=172331
DATABASE_PORT=5433
DATABASE_DATABASE=ClarkeEnergia

MODE_DEBUG=True
CORS_URI=http://localhost:3000
```

### **Frontend**
- **Linguagem**: JavaScript
- **Biblioteca**: React.js
- **Estilização**: CSS Modules
- **Comunicação com API**: GraphQL
- **Testes**: Jest

## Organização dos Arquivos
O projeto segue boas práticas de organização, separando código de frontend e backend em repositórios distintos.

- **backend/** → Contém toda a lógica do servidor e a API.
- **frontend/** → Implementação da interface do usuário.

## Como Executar o Projeto

### Executar com Manualmente
1. **Configurar o backend Manualmente** [Guia de Instalação do Backend](backend/README.md)
2. **Configurar o frontend Manualmente** [Guia de Instalação do Frontend](frontend/README.md)

### Executar com Docker
Para rodar o sistema completo utilizando Docker:


1. 1. Clone este repositório:
   ```bash
   git clone https://github.com/brunodealmeida17/ClarkeEnergia
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd ClarkeEnergia
   ```


3. Certifique-se de que os arquivos `.env` do backend e frontend estão configurados corretamente.
4. Execute os seguintes comandos:
   ```sh
   docker-compose up --build
   ```
5. O backend estará disponível em `http://localhost:5000` e o frontend em `http://localhost:3000`.

### Estrutura do `docker-compose.yml`
```yaml
services:
  db:
    image: postgres:15
    container_name: bancoenergia
    restart: always
    ports:
      - "5433:5432"
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: <senha>
      POSTGRES_DB: ClarkeEnergias
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      retries: 5

  backend:
    build:
      context: ./backend
    ports:
      - "5000:5000"
    volumes:
      - ./backend:/app
    environment:
      - FLASK_ENV=development
    env_file:
      - ./backend/.env
    depends_on:
      db:
        condition: service_healthy

  frontend:
    build:
      context: ./frontend
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
    environment:
      - NODE_ENV=development
    env_file:
      - ./frontend/.env
    depends_on:
      - backend 

volumes:
  postgres_data:

```

### Dockerfiles

**Backend (`Dockerfile`):**
```dockerfile
# Usar uma imagem base do Python
FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]
```

**Frontend (`Dockerfile`):**
```dockerfile
# Usar a imagem base do Node.js
FROM node:16

WORKDIR /app

COPY . /app
RUN mv .env-exemple .env

RUN npm install
RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
```

## Instalação do Docker

### Windows
1. Baixe e instale o [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. Certifique-se de ativar a opção de "WSL 2 based engine" nas configurações.
3. Reinicie o sistema se necessário.
4. Verifique se a instalação foi bem-sucedida executando:
   ```sh
   docker --version
   ```
5. Para iniciar o Docker, abra o Docker Desktop.

### Ubuntu
1. Atualize os pacotes do sistema:
   ```sh
   sudo apt update && sudo apt upgrade -y
   ```
2. Instale os pacotes necessários:
   ```sh
   sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
   ```
3. Adicione o repositório oficial do Docker:
   ```sh
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```
4. Instale o Docker:
   ```sh
   sudo apt update
   sudo apt install -y docker-ce docker-ce-cli containerd.io
   ```
5. Adicione seu usuário ao grupo `docker` para rodar sem `sudo`:
   ```sh
   sudo usermod -aG docker $USER
   ```
6. Reinicie a sessão ou o sistema.
7. Verifique se a instalação foi bem-sucedida executando:
   ```sh
   docker --version
   ```

Agora, o projeto está pronto para ser executado com Docker! 🚀

