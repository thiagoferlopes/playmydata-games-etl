#Importando biblioteca#
import pandas as pd
#=====================#


#Analisando a estrutura do arquivo#
df = pd.read_csv('data/raw/all_games_PC.csv')

print(df.head())
print(df.shape) 
print(df.columns)
print(df.info()) 
#=================================#