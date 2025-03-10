from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


# Configuração do banco de dados
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

print("Banco de dados iniciado!")
Base = declarative_base()


# Dependência para obter a sessão do banco de dados de usuários
def get_db_users():
    db_users = SessionLocal()
    try:
        yield db_users
    finally:
        db_users.close()