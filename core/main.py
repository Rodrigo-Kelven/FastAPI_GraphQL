from fastapi import FastAPI
from core.api.routes import routes

# Criando a aplicação FastAPI
app = FastAPI()

app.include_router(routes)

