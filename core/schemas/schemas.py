import strawberry
from core.config.config import Session, SessionLocal
from core.model.model import User

from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

# Definindo o tipo GraphQL
@strawberry.type
class Userlist(BaseModel):
    id: str
    username: str
    email: str
    password: str




# Função para obter todos os usuários do banco de dados
"""def get_users() -> list[UserList]:
    db: Session = SessionLocal()
    try:
        users = db.query(User).all()  # Obtém todos os usuários do banco de dados
        return [UserList.from_orm(user) for user in users]  # Converte cada usuário para o schema UserList
    finally:
        db.close()"""

# Função para obter itens do banco de dados
def get_users():
    db: Session = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users



# Definindo a consulta GraphQL
@strawberry.type
class Query_User:
    all_users: list[Userlist] = strawberry.field(resolver=get_users)



# Schema para o usuário
class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True

"""
# Schema para a postagem
class PostBase(BaseModel):
    content: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    user_id: int
    created_at: datetime
    comments: List["Comment"] = []
    likes: List["Like"] = []

    class Config:
        orm_mode = True

# Schema para o comentário
class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    post_id: int

class Comment(CommentBase):
    id: int
    user_id: int
    post_id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Schema para a curtida
class LikeBase(BaseModel):
    post_id: int

class LikeCreate(LikeBase):
    pass

class Like(LikeBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True"""