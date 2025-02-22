import strawberry
from fastapi import FastAPI, HTTPException
from strawberry.fastapi import GraphQLRouter
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Configuração do banco de dados
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definindo o modelo de dados
class ItemModel(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

# Criando as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Definindo o tipo GraphQL
@strawberry.type
class Item:
    id: int
    name: str
    description: str

# Função para obter itens do banco de dados
def get_items():
    db: Session = SessionLocal()
    items = db.query(ItemModel).all()
    db.close()
    return items

# Definindo a consulta GraphQL
@strawberry.type
class Query:
    all_items: list[Item] = strawberry.field(resolver=get_items)

# Criando o esquema GraphQL
schema = strawberry.Schema(query=Query)

# Criando a aplicação FastAPI
app = FastAPI()

# Adicionando a rota GraphQL
app.include_router(GraphQLRouter(schema), prefix="/graphql")

# Rota de saúde
@app.get("/")
def read_root():
    return {"message": "API GraphQL em FastAPI com SQLAlchemy"}

# Rota para adicionar um item
@app.post("/items/")
def create_item(name: str, description: str):
    db: Session = SessionLocal()
    new_item = ItemModel(name=name, description=description)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    db.close()
    return new_item