from config.config import Base, engine, SessionLocal, Session
from strawberry.fastapi import GraphQLRouter
from fastapi import APIRouter, HTTPException
from schemas.schemas import Query
from model.model import ItemModel
import strawberry
import uuid

routes = APIRouter(prefix="/api/v1")

# Criando as tabelas no banco de dados
Base.metadata.create_all(bind=engine)


# Criando o esquema GraphQL
schema = strawberry.Schema(query=Query)


# Adicionando a rota GraphQL
routes.include_router(GraphQLRouter(schema), prefix="/graphql")


# Rota de saúde
@routes.get("/")
def read_root():
    return {"message": "API GraphQL em FastAPI com SQLAlchemy"}


# Rota para adicionar um item
@routes.post("/items/")
def create_item(name: str, description: str):
    db: Session = SessionLocal()

    # passando o id como UUID
    item_id = str(uuid.uuid4())

    new_item = ItemModel(id=item_id,  name=name, description=description)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    db.close()
    return new_item