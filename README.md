
# FastAPI and GraphQL

## API GraphQL com FastAPI e Strawberry
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![FastAPI](https://img.shields.io/badge/FastAPI-%23FF4F00.svg?style=for-the-badge&logo=fastapi&logoColor=white)
![GraphQL](https://img.shields.io/badge/GraphQL-%23E10098.svg?style=for-the-badge&logo=graphql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white) 
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) 


 Este projeto é uma API GraphQL simples construída com FastAPI e Strawberry, duas ferramentas poderosas do ecossistema Python. A API permite que os usuários consultem uma lista de itens, cada um contendo um ID, username, fullName, email, role, hashedPassword, disabled, verified, createdAt.

## Sobre GraphQL
 O GraphQL é uma linguagem de consulta para APIs que oferece flexibilidade ao cliente, permitindo solicitar exatamente os dados necessários. Diferentemente do REST, onde múltiplas rotas são usadas para diferentes recursos, o GraphQL utiliza uma única rota que pode retornar diversos tipos de dados, otimizando a comunicação entre cliente e servidor.

## Sobre Strawberry

Strawberry é uma biblioteca de GraphQL para Python que utiliza anotações de tipo para criar APIs de maneira intuitiva e moderna. Ela se integra perfeitamente com o FastAPI, permitindo criar endpoints GraphQL com facilidade. O principal componente utilizado é o GraphQLRouter, que serve como ponto de entrada para as consultas GraphQL.

## Benefícios do Projeto

  - Flexibilidade: Clientes podem consultar apenas os dados necessários, reduzindo o tráfego de rede.
  - Simplicidade: Com Strawberry e FastAPI, a configuração da API é direta e eficiente.
  - Escalabilidade: A estrutura GraphQL facilita a adição de novos tipos de dados sem alterar a lógica existente.


### Versão: 1.2.11

#### Para mais informações sobre: 
* https://www.redhat.com/pt-br/topics/api/what-is-graphql
* https://graphql.org/learn/


## Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/): Um framework moderno e rápido para construir APIs com Python.
- [Strawberry](https://strawberry.rocks/): Uma biblioteca para criar APIs GraphQL em Python.
- [Uvicorn](https://www.uvicorn.org/): Um servidor ASGI para rodar a aplicação.

## Pré-requisitos

Antes de começar, você precisa ter o Python 3.7 ou superior instalado em sua máquina. Você também deve ter o `pip` para instalar as dependências.

## Instalação
```bash
  git clone https://github.com/Rodrigo-Kelven/FastAPI_GraphQL
  cd FastAPI_GraphQL
  pip install -r requirements.txt
```

## Usando via docker
```bash
  docker build -t api_graphql .
  docker run -p 8000:8000 api_graphql
```

### Usando a API

#### A API GraphQL pode ser acessada em http://127.0.0.1:8000/api/v1/graphql. Você pode usar a interface GraphQL para fazer consultas.

 -h## Exemplo de Consulta

#### Para obter todos os itens, você pode usar a seguinte consulta:

```bash
{
  allUsers {
    id
    username
    fullName
    email
    role
    hashedPassword
    disabled
    verified
    createdAt    
  }
}
```
## Resposta Esperada

#### A resposta para a consulta acima será semelhante a:

```bash
{
  "data": {
    "allUsers": [
      {
        "id": "61476a49-6f68-4ba0-998f-07196de68abe",
        "username": "string",
        "fullName": "string",
        "email": "user@example.com",
        "role": "Role.admin",
        "hashedPassword": "$2b$12$SjQvK5W9nE5UW9PnDsMRxOXqaKVG8.GRqtVIL/5ZeiAV33c5SV2M.",
        "disabled": false,
        "verified": 0,
        "createdAt": "2025-03-10T02:22:27"
      }
    ]
  }
}
```

# Contribuições
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir um issue ou enviar um pull request.;)

## Autores
- [@Rodrigo_Kelven](https://github.com/Rodrigo-Kelven)
