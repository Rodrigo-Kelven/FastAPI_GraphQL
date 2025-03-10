from core.db.config import Session, SessionLocal
from core.model.model import User
from pydantic import BaseModel
from datetime import datetime
import strawberry



# Definindo o tipo GraphQL
@strawberry.type
class Userlist(BaseModel):
    id: str
    username: str
    full_name: str
    email: str
    hashed_password: str
    disabled: bool
    role: str
    created_at: datetime
    verified: int


# Função para obter itens do banco de dados
def get_users():
    db: Session = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users


# Definindo a consulta GraphQL
@strawberry.type
class Query_User:
    allUsers: list[Userlist] = strawberry.field(resolver=get_users)

