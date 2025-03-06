# ClarkeEnergia-Frontend

## Descrição
Este é o frontend do sistema ClarkeEnergia, desenvolvido em React.js. Ele consome a API GraphQL para exibir e gerenciar fornecedores de energia, bem como capturar dados de consumo dos usuários.

## Estrutura do Projeto
```
frontend/
├── node_modules/              # Dependências do projeto
├── public/                    # Arquivos públicos
├── src/                       # Código-fonte principal
│   ├── components/           # Componentes React reutilizáveis
│   │   ├── FormularioConsumo.js
│   │   ├── Fornecedores.js
│   ├── graphql/              # Consultas GraphQL
│   │   ├── queries.js
│   ├── tests/                # Testes automatizados
│   │   ├── App.test.js
│   │   ├── Fornecedores.test.js
│   ├── App.css               # Estilos globais do App
│   ├── App.js                # Componente principal da aplicação
│   ├── index.css             # Estilos globais
│   ├── index.js              # Ponto de entrada do React
│   ├── logo.svg              # Logo do sistema
│   ├── reportWebVitals.js    # Monitoramento de performance
│   ├── setupTests.js         # Configuração de testes
├── .env-exemple              # Arquivo de exemplo para variáveis de ambiente
├── README.md                 # Documentação do projeto
├── package-lock.json         # Controle de versão das dependências
├── package.json              # Dependências e scripts do projeto
```

## Tecnologias Utilizadas
- React.js
- GraphQL (para comunicação com a API)
- Jest (para testes automatizados)
- CSS Modules (para estilização)

## Instalação e Configuração
1. Clone este repositório:
   ```bash
   git clone https://github.com/brunodealmeida17/ClarkeEnergia
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd ClarkeEnergia/frontend
   ```
3. Instale as dependências:
   ```bash
   npm install
   ```
4. Renomeie o arquivo .env-exemple para .env e configure as variáveis de ambiente conforme necessário. As variáveis de ambiente necessárias são as seguintes:
  ```bash
    REACT_APP_API_URL=http://localhost:5000/graphql
  ```

5. Inicie o servidor de desenvolvimento:
   ```bash
   npm start
   ```

## Scripts Disponíveis
No diretório do projeto, você pode executar:

- `npm start`: Inicia o projeto em modo desenvolvimento.
- `npm test`: Executa os testes automatizados.
- `npm run build`: Gera a versão otimizada para produção.
