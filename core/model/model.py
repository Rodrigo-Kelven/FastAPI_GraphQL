from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from core.config.config import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=False, index=True)
    email = Column(String, unique=False, index=True)
    password = Column(String)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    verified = Column(Integer, default=0)  # 0 = não verificado, 1 = verificado
