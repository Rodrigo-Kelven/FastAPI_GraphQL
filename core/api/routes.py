from core.schemas.schemas import UserCreate, UserResponse, UserBase
from core.schemas.schemas_graphql import Query_User
from strawberry.fastapi import GraphQLRouter
from fastapi import APIRouter
import strawberry


from core.services.service import UserService


# definindo prefixo da api
router = APIRouter(prefix="/api/v1")


# Criando o esquema GraphQL
schema = strawberry.Schema(query=Query_User)


# Adicionando a rota GraphQL
router.include_router(GraphQLRouter(schema), prefix="/graphql")


# Rota de saúde
@router.get("/")
def read_root():
    return {"message": "API GraphQL em FastAPI com SQLAlchemy"}


# Rota para adicionar um item
@router.post("/cadastro_user/", response_model=UserResponse)
def create_item(payload: UserCreate):

    return UserService.create_user(payload)
    #return UserService.response_create_user(user)


@router.delete("/delete_user/{id_user}")
def delete_user(id_user: str):
    return UserService.delete_user(id_user)


@router.get("/get_all_users", response_model=list[UserResponse])
def get_all_users():
    return UserService.get_all_users()


@router.put("/update_user{user_id}", response_model=UserResponse)
def update_user(payload: UserBase, user_id: str):
    return UserService.update_user(payload, user_id)


@router.delete("/delete_all_users")
def delete_all_users():
    UserService.delete_all_users()
    return {"message": "All users deleted successfully."}