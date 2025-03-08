from fastapi import FastAPI
from core.config.config import Base, engine

from core.api.routes import routes

# Criando as tabelas no banco de dados
Base.metadata.create_all(bind=engine)
print("Banco de dados criado com sucesso!")

# Criando a aplicação FastAPI
app = FastAPI()

app.include_router(routes)