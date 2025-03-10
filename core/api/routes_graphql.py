from core.schemas.schemas_graphql import Query_User
from strawberry.fastapi import GraphQLRouter
from fastapi import APIRouter
import strawberry

router_graphql = APIRouter(prefix="/api/v1", tags=["Api GraphQL"])


# Criando o esquema GraphQL
schema = strawberry.Schema(query=Query_User)


# Adicionando a rota GraphQL
router_graphql.include_router(GraphQLRouter(schema), prefix="/graphql")