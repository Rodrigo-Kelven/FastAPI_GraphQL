from core.schemas.schemas import UserResponse, UserCreate
from core.config.config import SessionLocal
from fastapi import HTTPException, status
from core.model.model import User
from sqlalchemy import select
import uuid


# implementar todas as operacoes realizadas pelo usuario nesta  classe
class UserService:

    # veirifca se ja existe usuario com email ja cadastrado na Tabela User
    @staticmethod
    def check_email_exists(email: str, db):
        # Verifica se o email já existe no banco de dados
        existing_user = db.execute(select(User).where(User.email == email)).scalar()
        return existing_user
    
    
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

        # Passando o id como UUID
        user_id = str(uuid.uuid4())

        # Criando item no banco
        new_user = User(
            id=user_id, 
            username=payload.username,
            email=payload.email,
            password=payload.password
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
    def delete_user(id_user: str):
        # varival responsavel por pegar a sessao com o banco de dados
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
    def update_user(payload: UserCreate, user_id: str):
        # varival responsavel por pegar a sessao com o banco de dados
        db = SessionLocal()

        # verifica se o usuario existe
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            db.close()
            raise HTTPException(status_code=404, detail="User  not found")

        """
        Quando se faz um PUT, nao precisa passar o modelo da tabela do DB
        Porque a variavel user é declarada, ela ja recebe todo o modelo
        Assim so precisa passar os dados novos e realizar o "update"
        """
        user.username = payload.username
        user.email = payload.email

        db.commit()
        db.refresh(user)
        db.close()
        # nao esqueca de retornar, senao retornar o valor aqui, como ira aparecer no response_model ??
        return user
    

    @staticmethod
    def delete_all_users():
        db = SessionLocal()
        try:
            db.query(User).delete()  # Deleta todos os usuários
            db.commit()  # Confirma a transação
        except Exception as e:
            db.rollback()  # Reverte a transação em caso de erro
            raise e
        finally:
            db.close()  # Fecha a sessão