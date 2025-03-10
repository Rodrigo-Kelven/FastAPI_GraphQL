from core.db.config import SessionLocal
from core.model.model import User
from datetime import datetime
import strawberry
from fastapi import FastAPI, HTTPException, Request
from strawberry.fastapi import GraphQLRouter
from graphql import parse


# Definindo o tipo GraphQL
@strawberry.type
class Userlist:
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
def get_users() -> list[Userlist]:
    db = SessionLocal()
    try:
        users = db.query(User).all()
        return [Userlist(
            id=user.id,
            username=user.username,
            full_name=user.full_name,
            email=user.email,
            hashed_password=user.hashed_password,
            disabled=user.disabled,
            role=user.role,
            created_at=user.created_at,
            verified=user.verified
        ) for user in users]
    finally:
        db.close()


# Função para verificar a profundidade da consulta
def check_query_depth(query: str, max_depth: int = 3):
    parsed_query = parse(query) # Analisa a consulta GraphQL em uma estrutura de árvore
    depth = 0 # Inicializa a profundidade

    def traverse(node, current_depth):
        nonlocal depth # Permite que a função interna acesse a variável depth
        if hasattr(node, 'selection_set'): # Verifica se o nó tem um conjunto de seleções
            current_depth += 1 # Aumenta a profundidade atual
            depth = max(depth, current_depth) # Atualiza a profundidade máxima
            for selection in node.selection_set.selections: # Itera sobre as seleções
                traverse(selection, current_depth) # Chama recursivamente para cada seleção

    traverse(parsed_query, 0) # Inicia a travessia a partir da raiz da consulta
    if depth > max_depth: # Verifica se a profundidade máxima foi excedida
        raise HTTPException(status_code=400, detail="Query depth exceeds maximum allowed depth.")


# Definindo a consulta GraphQL
@strawberry.type
class Query_User:
    all_users: list[Userlist] = strawberry.field(resolver=get_users)


# Definindo a consulta GraphQL
@strawberry.type
class Query_User:
    allUsers: list[Userlist] = strawberry.field(resolver=get_users)

