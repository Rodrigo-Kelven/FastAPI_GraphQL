from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# Schema para o usuário
class UserBase(BaseModel):
    username: str
    full_name: str
    email: EmailStr

    class Config:
        orm_mode = True

# Schema para o usuário
class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


# schema completo para responder a requisicao
class UserResponse(BaseModel):
    id: str
    username: str
    full_name: str
    email: EmailStr
    disabled: bool
    role: str
    created_at: datetime
    verified: int

# sem uso no momento
class UserResponseUpdate(BaseModel):
    id: str
    username: str
    full_name: str
    email: EmailStr
    disabled: bool
    role: str
    created_at: datetime
    verified: int


# Modelos Pydantic para validação
class Token(BaseModel):
    access_token: str
    token_type: str


# usado em auth 
class TokenData(BaseModel):
    username: str

