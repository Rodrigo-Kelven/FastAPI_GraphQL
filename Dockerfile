FROM python:3.12-slim

# copia tudo
COPY . .

# instala as dependencias
RUN pip install --no-cache-dir -r core/requirements.txt

# expoen a porta 8000 para a aplicacao
EXPOSE 8000

# rora o comando nescessario da api
CMD ["uvicorn", "core.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]