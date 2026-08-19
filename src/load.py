#Importando bibliotecas:
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

#============================#
#Carrega a função do dotenv que carrega as variáveis do .env:
load_dotenv()

#============================#
#Definindo a função "get_engine" sem parámetros:
def get_engine():

#============================#
#Carrega as variáveis carregadas da função do "load_dotenv()":
    usuario = os.getenv('DB_USER')
    senha = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    porta = os.getenv('DB_PORT')
    nome_banco = os.getenv('DB_NAME')

#============================#
#Monta a string de conexão usando f-strings:
    DATABASE_URL = f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{nome_banco}"

#============================#
#Imprime o URL de conexão com a senha mascarada:
    print(DATABASE_URL.replace(senha, "***"))

#============================#
#Cria o objeto engine, passando a URL montada:
    engine = create_engine(DATABASE_URL)

#============================#
#Retorna a engine ;)
    return engine

#============================#
#Verifica se esse arquivos está sendo exportado diretamente em src/load.py:
if __name__ == '__main__':
    engine = get_engine()
    
    try:
        with engine.connect() as conn:
            print('SUCESSO')
    except Exception as e:
        print(f'FALHA: {e}')

#============================#
