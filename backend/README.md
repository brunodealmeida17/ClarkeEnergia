# ClarkeEnergia-backend

## Descrição
Este é o backend do sistema ClarkeEnergia, desenvolvido em Python, utilizando Flask como framework principal. O projeto gerencia fornecedores de energia e suas respectivas informações e disponibiliza uma API baseada em GraphQL para manipulação dos dados.

## Estrutura do Projeto
```
backend/
├── migrations/               # Diretório de migrações do banco de dados (Alembic)
│   ├── versions/            # Versões das migrações
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
├── models/                   # Modelos de dados
│   ├── __init__.py
│   ├── fornecedor.py         # Modelo do fornecedor
├── schema/                   # Schemas para validação de dados
│   ├── __init__.py
│   ├── fornecedor_schema.py  # Schema do fornecedor
├── static/logos/             # Diretório para logos
├── tests/                    # Testes automatizados
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_fornecedor.py
├── .env-exemple              # Arquivo de exemplo para variáveis de ambiente
├── config.py                 # Configuração do projeto
├── main.py                   # Ponto de entrada da aplicação
├── requirements.txt          # Dependências do projeto
├── utils.py                  # Funções utilitárias
```

## Tecnologias Utilizadas
- Python
- Flask
- Flask-CORS (para permitir requisições de diferentes origens)
- Flask-GraphQL (para implementação de API GraphQL)
- Flask-Migrate (para controle de migração do banco de dados)
- Flask-SQLAlchemy (ORM para interação com o banco de dados)
- Graphene (framework GraphQL para Python)
- Graphene-File-Upload (para upload de arquivos via GraphQL)
- PostgreSQL (banco de dados)
- SQLAlchemy (mapeamento objeto-relacional)
- Psycopg2-Binary (driver para PostgreSQL)
- Python-Dotenv (gerenciamento de variáveis de ambiente)
- Pytest (para testes automatizados)

## Instalação e Configuração
1. Clone este repositório:
   ```bash
   git clone https://github.com/brunodealmeida17/ClarkeEnergia
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd ClarkeEnergia/backend
   ```
3. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Renomeie o arquivo .env-exemple para .env e configure as variáveis de ambiente conforme necessário. As variáveis de ambiente necessárias são as seguintes:

> **Nota:** O banco de dados utilizado depende da variável `MODE_DEBUG` no arquivo `.env` do backend:
> - Se `MODE_DEBUG=True`, o banco de dados SQLite será utilizado, ideal para testes automatizados.
> - Se `MODE_DEBUG=False`, o PostgreSQL será utilizado para ambiente de produção.

  ```bash
    DATABASE_HOST=localhost
    DATABASE_USER=postgres
    DATABASE_PASSWORD=root
    DATABASE_PORT=5432
    DATABASE_DATABASE=DatabaseName
    MODE_DEBUG=True
  ```

6. Execute as migrações do banco de dados:
   ```bash
   flask db upgrade
   ```
7. Inicie o servidor:
   ```bash
   python main.py
   ```

## Endpoints da API (GraphQL)
Todas as requisições para manipulação de dados são feitas via **GraphQL API** no endpoint `/graphql`.

### Criar um fornecedor
```graphql
mutation ($file: Upload!, $nome: String!, $estado: String!, $custoPorKwh: Float!, $limiteMinimoKwh: Int!, $numClientes: Int!, $avaliacaoMedia: Float!) {
  createFornecedor(nome: $nome, estado: $estado, custoPorKwh: $custoPorKwh, limiteMinimoKwh: $limiteMinimoKwh, numClientes: $numClientes, avaliacaoMedia: $avaliacaoMedia, logo: $file) {
    fornecedor {
      id
      nome
      logo
    }
  }
}
```

### Buscar todos os fornecedores de acordo com o Limite minino em Kwh
```graphql
query {
  fornecedores(limiteMinimoKwh: 500) {
    id
    nome
    estado
    custoPorKwh
    limiteMinimoKwh
    numClientes
    avaliacaoMedia
    logo
  }
}
```

### Buscar um fornecedor por ID
```graphql
query ($id: Int!) {
  fornecedor(id: $id) {
    id
    nome
    estado
    custoPorKwh
    logo
  }
}
```

### Atualizar um fornecedor
```graphql
mutation ($id: Int!, $nome: String, $estado: String) {
  updateFornecedor(id: $id, nome: $nome, estado: $estado) {
    fornecedor {
      id
      nome
      estado
    }
  }
}
```

### Excluir um fornecedor
```graphql
mutation ($id: Int!) {
  deleteFornecedor(id: $id) {
    success
  }
}
```

