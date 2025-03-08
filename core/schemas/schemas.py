import strawberry
from core.config.config import Session, SessionLocal
from core.model.model import ItemModel


# Definindo o tipo GraphQL
@strawberry.type
class Item:
    id: str
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

