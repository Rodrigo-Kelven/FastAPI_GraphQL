from core.api.routes import router
from core.api.routes_graphql import router_graphql
from fastapi import APIRouter

all_router = APIRouter()

# organizando e separando as duas apis 
def routes(app):
    app.include_router(router)
    app.include_router(router_graphql)