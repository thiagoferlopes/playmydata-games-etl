#Importando as bibliotecas:
import pandas as pd
import numpy as np

#============================#
#Definindo da função 'transform':
def transform(df: pd.DataFrame) -> pd.DataFrame:

#============================#
#Selecionando somente as colunas desejadas:
    colunas_desejadas = [
        'id',
        'name',
        'summary',
        'storyline',
        'rating',
        'main',
        'extra',
        'completionist',
        'review_score',
        'review_count',
        'people_polled',
    ]

    df = df[colunas_desejadas]

#============================#
#Renomeando algumas colunas para deixar mais claro do que se trata:
    df = df.rename(
        columns={
            'main': 'main_hours',
            'extra': 'extra_hours',
            'completionist': 'completionist_hours',
        }
    )

#============================#
#Limpeza de valores nulos

    df = df.replace('Missing', np.nan)
    
#============================#
#Transformando colunas númericas e evitando erros na execução:

    colunas_numericas = [
        'rating',
        'main_hours',
        'extra_hours',
        'completionist_hours',
        'review_score',
        'review_count',
        'people_polled',
    ]
    for coluna in colunas_numericas:
        df[coluna] = pd.to_numeric(df[coluna], errors='coerce')

#============================#
#Removendo registros duplicados por id:
    df = df.drop_duplicates(
        subset=['id']
    )

#============================#
#Ordenando por avaliação em ordem decrescente
    df = df.sort_values(
        by='rating',
        ascending=False
    )

#============================#
#Retornando o dataframe :)
    return df

#============================#
