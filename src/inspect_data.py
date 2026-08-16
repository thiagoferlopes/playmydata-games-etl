#Puxa as funções de outra tabela
from transform import transform
from extract import extract

#Utiliza as funções para extrair e transformar o dataset
df = extract('data/raw/all_games_PC.csv')
df = transform(df)

#Removo todo o registro que tiver ou ID ou NOME nulo
df = df.dropna(subset=['id', 'name'])

#Transformo os registros de quantidade de avaliações de NULO para ZERO
df['review_count'] = df['review_count'].fillna(0)

#Imprimo todas as colunas mostrando a quantidade de nulos em cada uma delas
print(df.isna().sum())