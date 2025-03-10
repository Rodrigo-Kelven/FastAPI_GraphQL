from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware



# Configurações e chave secreta

# Use este comando para gerar sua chave caso queira: openssl rand -hex 64
# sim esta chave é uma chave inutilizavel
# NÃO PODE SUBIR SUAS CHAVES PRIVADAS PARA O REPOSITORIO!!
SECRET_KEY = "58da576fa5c438016e3e8d569b9a088449db601b73d8124ffa73e2f8558240a0202c449850742108e001fb422b5ed7250031435e6d4155af421292c0754dd749"
ALGORITHM = "HS256" # algoritmo para a criptografia dos passwords
ACCESS_TOKEN_EXPIRE_MINUTES = 60 # tempo de expiracao do token

# Inicialização de FastAPI e outras configurações
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# O usuário digita o username e a senha no frontend e aperta Enter.
# O frontend (rodando no browser do usuário) manda o username e a senha para uma URL específica na sua API (declarada com tokenUrl="token").
# Esse parâmetro contém a URL que o client (o frontend rodando no browser do usuário) vai usar para mandar o username e senha para obter um token
# se mudar a rota de login, nao esqueca de mudar aqui, porque o fastapi simplesmente nao AVISA PORRA
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login") 



def cors(app):
    from fastapi.middleware.cors import CORSMiddleware

    origins = [
        "http://localhost.tiangolo.com",
        "https://localhost.tiangolo.com",
        "http://localhost:5173/", # react
        "http://localhost:8080",
    ]

    app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
    expose_headers=["X-Custom-Header"],
    max_age=3600,
)