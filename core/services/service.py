from core.schemas.schemas import UserResponse, UserCreate
from core.db.config import SessionLocal, get_db_users
from fastapi import Depends, HTTPException, status
from core.model.model import User, Role
from sqlalchemy import select
import uuid

from typing import List, Annotated


from core.auth.auth import get_password_hash, get_current_active_user, get_user, check_permissions


# implementar todas as operacoes realizadas pelo usuario nesta  classe
class UserService:

    # veirifca se ja existe usuario com email ja cadastrado na Tabela User
    @staticmethod
    def check_email_exists(email: str, db):
        # Verifica se o email já existe no banco de dados
        existing_user = db.execute(select(User).where(User.email == email)).scalar()
        return existing_user
    

    # veirifca se ja existe usuario com username ja cadastrado na Tabela User
    @staticmethod
    def check_username_exists(username: str, db):
        # Verifica se o email já existe no banco de dados
        existing_user = db.execute(select(User).where(User.username == username)).scalar()
        return existing_user
    

    # veirifca se ja existe usuario com full_name ja cadastrado na Tabela User
    @staticmethod
    def check_full_name_exists(full_name: str, db):
        # Verifica se o email já existe no banco de dados
        existing_user = db.execute(select(User).where(User.full_name == full_name)).scalar()
        return existing_user
    
    
    # sem Uso
    @staticmethod
    def response_create_user(user: User) -> UserResponse:
        # Resposta ao criar usuário, caso nao use o response model
        return UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            created_at=user.created_at,
            verified=user.verified
        )
    

    # Criar o usuário na tabela User
    @staticmethod 
    def create_user(payload: UserCreate):
        # varival responsavel por pegar a sessao com o banco de dados
        db = SessionLocal()
        
        # Verifica se o email já existe
        if UserService.check_email_exists(payload.email, db):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email já está em uso.")
        
        if UserService.check_username_exists(payload.username, db):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Este usuario já existe!")
        
        if UserService.check_full_name_exists(payload.full_name, db):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Full Name ja registrado!")

        # Passando o id como UUID
        user_id = str(uuid.uuid4())

        # Criando item no banco
        hash_password = get_password_hash(payload.password)
        new_user = User(
            id=user_id, 
            username=payload.username,
            full_name=payload.full_name,
            email=payload.email,
            hashed_password=hash_password
        )

        try:
            db.add(new_user)
            db.commit()
            db.refresh(new_user)

            # retornando o valor aqui, no response model será exibido
            return new_user
            #return UserService.response_create_user(new_user)  # Retorna a resposta formatada
        except Exception as e:
            db.rollback()  # Rollback em caso de erro
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        finally:
            db.close()

    

    # deleta usuario 'com id_user' do banco User
    @staticmethod
    def delete_user(current_user: Annotated[User , Depends(get_current_active_user)]):
        # varival responsavel por pegar a sessao com o banco de dados
        db = SessionLocal()
        db_user = get_user(db, current_user.username)  # Obtém o usuário autenticado

        if not db_user:
            db.close()
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario nao encontrado!")
        
        try:
            # Exclui o usuário
            db.delete(db_user)
            db.commit()
            return {"detail": "Usuário excluído com sucesso."}
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        finally:
            db.close()


        

    
    # pega todos os usuarios do banco User
    @staticmethod
    def get_all_users():
        # varival responsavel por pegar a sessao com o banco de dados
        db = SessionLocal()

        users = db.query(User).all()
        db.close()
        # sera renderizado no response_model
        return users
    

    @staticmethod
    def update_user(payload: UserCreate, current_user):
        # varival responsavel por pegar a sessao com o banco de dados
        db = SessionLocal()
        db_user = get_user(db, current_user.username)  # Obtém o usuário autenticado

        if not db_user:
            db.close()
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario nao encontrado!")
        


        """
        Quando se faz um PUT, nao precisa passar o modelo da tabela do DB
        Porque a variavel user é declarada, ela ja recebe todo o modelo
        Assim so precisa passar os dados novos e realizar o "update"
        """
        db_user.username = payload.username
        db_user.email = payload.email

        db.commit()
        db.refresh(db_user)
        db.close()
        # nao esqueca de retornar, senao retornar o valor aqui, como ira aparecer no response_model ??
        return db_user
    

    @staticmethod
    def delete_all_users(current_user):
        db = SessionLocal()

        check_permissions(current_user, Role.admin)
        

        try:
            db.query(User).delete()  # Deleta todos os usuários
            db.commit()  # Confirma a transação
        except Exception as e:
            db.rollback()  # Reverte a transação em caso de erro
            raise e
        finally:
            db.close()  # Fecha a sessão