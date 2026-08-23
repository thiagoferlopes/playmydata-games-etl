#Importando a função de cada módulo da pipeline e logging:
import logging
from extract import extract
from transform import transform
from validate import validate
from load import loading, get_engine

#============================#
#Direcionando para onde cada registro de logs será enviado
logging.basicConfig(
    filename= 'logs/pipeline.log',
    level= logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s"
)
#============================#
#Definindo a função main
def main():

#============================#
#Caminho do arquivo CSV bruto usado para extração:
    caminho_csv = 'data/raw/all_games_PC.csv'

#============================#
#Extraindo o arquivo CSV bruto para um DataFrame, registrando o resultado no log::
    try:
        df = extract(caminho_csv)
        logging.info('Extração concluída com sucesso.')
    except FileNotFoundError as e:
        logging.error(f'Erro na extração: {e}')
        raise

#============================#
#Transformando o DataFrame (tipos, nulos, seleção de colunas, duplicados, ordenação) e adcionando o evento em logs:
    df = transform(df)
    logging.info('Transformação concluída.')

#============================#
#Retorna uma lista de erros encontrados
    erros = validate(df)

#============================#
#Se existirem erros, imprime cada um e interrompe o pipeline sem carregar nada e envia o problema para logs:
    if erros:
        for erro in erros:
            logging.error(erro)
        return

#============================#
#Se não existir nenhum erro, cria a conexão e carrega os dados para o PostgreSQL enviando o evento para logs:
    else:
        try:
            engine = get_engine()
            loading(df, engine)
            logging.info('Carga concluída com sucesso.')
            print('SUCESSO!')
        except Exception as e:
            logging.error(f'Erro na carga: {e}')
            raise
        
#============================#
#Executa o main somente quando esse arquivo é rodado diretamente:
if __name__ == "__main__":
    main()

#============================#
