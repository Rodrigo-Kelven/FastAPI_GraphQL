from core.schemas.schemas import UserCreate, UserResponse, UserBase
from core.services.service import UserService
from fastapi import APIRouter


# definindo prefixo da api
router = APIRouter(prefix="/api/v1", tags=["Api Rest"])


# Rota de saúde
@router.get(
        path="/",
        description="Rota home.",
        name="Route Home."
        )
def read_root():
    return {"message": "API GraphQL em FastAPI com SQLAlchemy"}


# Rota para adicionar um item
@router.post(
        path="/cadastro_user/",
        response_model=UserResponse,
        description="Rota para cadastro de usuarios.",
        name="Route for cadastro of users."
        )
def create_item(payload: UserCreate):
    # este payload, será enviado para a funcao,
    # e na propria funcao, será retornado o valor que será retornado no response_model
    return UserService.create_user(payload)


@router.delete(
        path="/delete_user/{id_user}",
        description="Rota para delete de usuarios.",
        name="Route for delete of users."
        )
def delete_user(id_user: str):
    # somente será passado o id do usuario para a operacao
    return UserService.delete_user(id_user)


@router.get(
        path="/get_all_users",
        response_model=list[UserResponse],
        description="Rota para pegar todos os usuarios registrados",
        name="Route for get all users registrateds."
        )
def get_all_users():
    return UserService.get_all_users()


@router.put(
        path="/update_user{user_id}",
        response_model=UserResponse,
        description="Rota para update de dados do usuario.",
        name="Route for update of datas of user."
        )
def update_user(payload: UserBase, user_id: str):
    return UserService.update_user(payload, user_id)


@router.delete(
        path="/delete_all_users",
        description="Rota para deletar todo os usuarios do banco de uam unica vez.",
        name="Route delet all datas of banc."
        )
def delete_all_users():
    UserService.delete_all_users()
    return {"message": "All users deleted successfully."}