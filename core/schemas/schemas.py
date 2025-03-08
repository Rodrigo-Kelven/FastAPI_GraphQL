from pydantic import BaseModel, EmailStr
from datetime import datetime


# Schema para o usuário
class UserBase(BaseModel):
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

# Schema para o usuário
class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
    created_at: datetime
    verified: int