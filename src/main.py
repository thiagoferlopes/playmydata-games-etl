#Importando a função de cada módulo da pipeline:
from extract import extract
from transform import transform
from validate import validate
from load import loading, get_engine

#============================#
#Definindo a função main
def main():

#============================#
#Caminho do arquivo CSV bruto usado para extração:
    caminho_csv = 'data/raw/all_games_PC.csv'

#============================#
#Extraindo o arquivo CSV bruto para um DataFrame:
    df = extract(caminho_csv)

#============================#
#Transformando o DataFrame (tipos, nulos, seleção de colunas, duplicados, ordenação):
    df = transform(df)
    
#============================#
#Retorna uma lista de erros encontrados
    erros = validate(df)

#============================#
#Se existirem erros, imprime cada um e interrompe o pipeline sem carregar nada:
    if erros:
        for erro in erros:
            print(erro)
        return

#============================#
#Se não existir nenhum erro, cria a conexão e carrega os dados para o PostgreSQL:
    else:
        engine = get_engine()
        loading(df, engine)
        print('SUCESSO!')
        
#============================#
#Executa o main somente quando esse arquivo é rodado diretamente:
if __name__ == "__main__":
    main()

#============================#
