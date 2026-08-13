import pandas as pd
df = pd.read_csv('data/raw/all_games_PC.csv')

print(df.head()) #Imprime as primeiras linhas

print(df.shape)#Imprime a quantidade de linhas e colunas

print(df.columns) #Imprime os nomes das colunas

print(df.info()) #Imprime informações (Ex: número, texto, data e etc)