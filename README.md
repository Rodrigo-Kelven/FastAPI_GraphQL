
# FastAPI and GraphQL

## API GraphQL com FastAPI e Strawberry

Este projeto é uma API GraphQL simples construída com FastAPI e Strawberry. A API permite que os usuários consultem uma lista de itens, cada um com um ID, nome e descrição. 

GraphQL é uma linguagem de consulta para APIs que permite que os clientes solicitem exatamente os dados de que precisam. Ao contrário do REST, onde você tem várias rotas para diferentes recursos, no GraphQL você tem uma única rota que pode retornar diferentes tipos de dados.

### Versão: 0.0.2

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

### Usando a API

#### A API GraphQL pode ser acessada em http://127.0.0.1:8000/graphql. Você pode usar a interface GraphQL para fazer consultas.

## Exemplo de Consulta

#### Para obter todos os itens, você pode usar a seguinte consulta:

```bash
{
  allItems {
    id
    name
    description
  }
}
```
## Resposta Esperada

#### A resposta para a consulta acima será semelhante a:

```bash
{
  "data": {
    "allItems": [
      {
        "id": 1,
        "name": "Item 1",
        "description": "Descrição do Item 1"
      },
      {
        "id": 2,
        "name": "Item 2",
        "description": "Descrição do Item 2"
      }
    ]
  }
}
```

# Contribuições
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir um issue ou enviar um pull request.;)

## Autores
- [@Rodrigo_Kelven](https://github.com/Rodrigo-Kelven)
