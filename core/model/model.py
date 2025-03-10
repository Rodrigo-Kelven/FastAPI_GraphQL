from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from core.db.config import Base
from enum import Enum as PyEnum



# Definindo os papéis possíveis (Role)
class Role(PyEnum):
    admin = "admin"
    user = "user"
    moderator = "moderator"


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, primary_key=True, unique=True, index=True, doc="Username do usuario, deve ser unico!")
    full_name = Column(String, index=True, unique=True,doc="Nome completo do user")
    email = Column(String, unique=True, index=True, doc="Email do usuario, deve ser unico!")
    hashed_password = Column(String, doc="A senha do usuario é salva criptografada")
    disabled = Column(Boolean, default=False, doc="Estado do usuario, ativo/inativo")
    # caso queira criar um usuario admin, modifique aqui, ou na rota post
    role = Column(SQLAlchemyEnum(Role), default=Role.admin, doc="Permissões do usuário: 'user', 'admin', ou 'moderator'")
        
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    verified = Column(Integer, default=0)  # 0 = não verificado, 1 = verificado

