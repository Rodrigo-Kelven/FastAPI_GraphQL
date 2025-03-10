from fastapi import FastAPI
from core.db.config import Base, engine

from core.api.routes import router
from core.api.all_routes import routes

# Criando as tabelas no banco de dados
Base.metadata.create_all(bind=engine)
print("Banco de dados criado com sucesso!")

# Criando a aplicação FastAPI
app = FastAPI()

routes(app)


"""
Organizar todas as rotas e adicionar descricao
Melhorar CRUD
ADD banco de dados MongoDB
ADD banco de dados Redis (caching)
Melhorar designer SOLID "adicionar verificacoes mais seguras"
ADD Loggs de monitoramento
ADD Autenticacao
"""