from sqlalchemy import select
from core.config.config import SessionLocal
from core.schemas.schemas import UserResponse, UserCreate
from fastapi import HTTPException, status
from core.model.model import User
import uuid

class UserService:

    @staticmethod
    def check_email_exists(email: str, db):
        # Verifica se o email já existe no banco de dados
        existing_user = db.execute(select(User).where(User.email == email)).scalar()
        return existing_user
    
    
    @staticmethod
    def response_create_user(user: User) -> UserResponse:
        # Resposta ao criar usuário
        return UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            created_at=user.created_at,
            verified=user.verified
        )
    

    @staticmethod 
    def create_user(payload: UserCreate):
        # Criar o usuário
        db = SessionLocal()
        
        # Verifica se o email já existe
        if UserService.check_email_exists(payload.email, db):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email já está em uso.")

        # Passando o id como UUID
        item_id = str(uuid.uuid4())

        # Criando item no banco
        new_user = User(
            id=item_id, 
            username=payload.username,
            email=payload.email,
            password=payload.password
        )

        try:
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return UserService.response_create_user(new_user)  # Retorna a resposta formatada
        except Exception as e:
            db.rollback()  # Rollback em caso de erro
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        finally:
            db.close()


    @staticmethod
    def delete_user(id_user: str):

        db = SessionLocal()
        
        try:
            # Verifica se o usuário existe
            user = db.execute(select(User).where(User.id == id_user)).scalar()
            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado.")


            # Exclui o usuário
            db.delete(user)
            db.commit()
            return {"detail": "Usuário excluído com sucesso."}
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        finally:
            db.close()


    