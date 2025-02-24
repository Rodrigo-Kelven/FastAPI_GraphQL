from sqlalchemy import create_engine, Column, String
from config.config import Base


# Definindo o modelo de dados
class ItemModel(Base):
    __tablename__ = "items"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)