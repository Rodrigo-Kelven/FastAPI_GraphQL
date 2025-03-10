from fastapi import APIRouter, Depends, HTTPException, status, Form, Body
from core.schemas.schemas import UserCreate, UserResponse, UserBase, Token, UserResponse
from fastapi.security import OAuth2PasswordRequestForm
from core.db.config import SessionLocal, get_db_users
from core.services.service import UserService
from core.model.model import User, Role
from typing import Annotated
from core.auth.auth import (
    authenticate_user, timedelta, ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token, get_current_active_user, check_permissions
)

# definindo prefixo da api
router = APIRouter(prefix="/api/v1", tags=["Api Rest"])



# rota login, esta rota recebe os dados do front para a validacao
@router.post(
        path="/login",
        response_description="Informations of login",
        description="Route login user",
        name="Route login user"
)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:

    db = SessionLocal()
    user = authenticate_user(db, form_data.username, form_data.password)
    db.close()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "role": user.role}, 
        expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


# Rota de saúde
@router.get(
        path="/",
        description="Rota home.",
        name="Route Home."
        )
def read_root():
    return {"message": "API GraphQL em FastAPI com SQLAlchemy"}


# Rota para adicionar um user
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


# rora para deletar usuario, somente logado
@router.delete(
        path="/delete_user/{id_user}",
        description="Rota para delete de usuarios.",
        name="Route for delete of users."
        )
def delete_user(current_user: Annotated[User , Depends(get_current_active_user)]):
    # somente com o usuario autenticaco/logado
    return UserService.delete_user(current_user)


# rota para pegar todos os usuarios, somente logado e sendo admin
@router.get(
        path="/get_all_users",
        response_model=list[UserResponse],
        description="Rota para pegar todos os usuarios registrados",
        name="Route for get all users registrateds."
        )
def get_all_users(
    current_user: Annotated[UserResponse, Depends(get_current_active_user)]
    ):
    check_permissions(current_user, Role.admin)  # Aqui verificamos se o usuário tem o papel de 'user'
    return UserService.get_all_users()


# rota para atualizar dados do usuario, somente logado
@router.put(
        path="/update_user",
        response_model=UserResponse,
        description="Rota para update de dados do usuario.",
        name="Route for update of datas of user."
        )
def update_user(
    payload: UserBase,
    current_user: Annotated[UserResponse, Depends(get_current_active_user)]
    ):
    return UserService.update_user(payload, current_user)


# rota para apagar todos os dados, somente admin e estando logado
# rota para testes, sera descartada
# uso somente para nao precisar apagar o db 
@router.delete(
        path="/delete_all_users",
        description="Rota para deletar todo os usuarios do banco de uam unica vez.",
        name="Route delet all datas of banc."
        )
def delete_all_users(current_user: Annotated[UserResponse, Depends(get_current_active_user)]):
    UserService.delete_all_users(current_user)
    return {"message": "All users deleted successfully."}