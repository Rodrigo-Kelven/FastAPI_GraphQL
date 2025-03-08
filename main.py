from fastapi import FastAPI
from api.routes import routes

# Criando a aplicação FastAPI
app = FastAPI()

app.include_router(routes)

