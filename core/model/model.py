from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from core.config.config import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=False, index=True)
    email = Column(String, unique=False, index=True)
    password = Column(String)
    
    #created_at = Column(DateTime(timezone=True), server_default=func.now())
    #verified = Column(Integer, default=0)  # 0 = não verificado, 1 = verificado

    """posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")
    likes = relationship("Like", back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User ", back_populates="posts")
    comments = relationship("Comment", back_populates="post")
    likes = relationship("Like", back_populates="post")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    content = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User ", back_populates="comments")
    post = relationship("Post", back_populates="comments")


class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User ", back_populates="likes")
    post = relationship("Post", back_populates="likes")"""