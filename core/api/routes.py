from core.schemas.schemas import UserCreate, UserResponse
from core.schemas.schemas_graphql import Query_User
from strawberry.fastapi import GraphQLRouter
from fastapi import APIRouter
import strawberry


from core.services.service import UserService


# definindo prefixo da api
routes = APIRouter(prefix="/api/v1")


# Criando o esquema GraphQL
schema = strawberry.Schema(query=Query_User)


# Adicionando a rota GraphQL
routes.include_router(GraphQLRouter(schema), prefix="/graphql")


# Rota de saúde
@routes.get("/")
def read_root():
    return {"message": "API GraphQL em FastAPI com SQLAlchemy"}


# Rota para adicionar um item
@routes.post("/cadastro_user/")
def create_item(payload: UserCreate):

    user = UserService.create_user(payload)
    return UserService.response_create_user(user)


@routes.delete("/delete_user/{id_user}")
def delete_user(id_user: str):
    return UserService.delete_user(id_user)