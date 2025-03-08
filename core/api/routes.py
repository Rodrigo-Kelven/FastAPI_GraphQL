from core.config.config import SessionLocal, Session
from strawberry.fastapi import GraphQLRouter
from fastapi import APIRouter, HTTPException
from core.schemas.schemas import UserBase, Query_User
from core.model.model import User
import strawberry
import uuid



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
def create_item(user: UserBase):
    db: Session = SessionLocal()

    # passando o id como UUID
    item_id = str(uuid.uuid4())

    # criando item no banco
    new_item = User(
        id=item_id, 
        username=user.username,
        email=user.email,
        password=user.password
        )
    
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    db.close()
    return new_item