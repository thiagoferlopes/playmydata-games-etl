#Definindo a função "validate"
def validate(df):

#============================#
#Lista para acumular erros encontrados no dataframe
    erros = []

#============================#
#Verifica se o DataFrame está vazio:
    if df.empty is True:
       erros.append('DataFrame vazio')

#============================#
#Verifica se tem algum id nulo no dataframe:
    if df['id'].isna().any():
        erros.append('Existe item nulo em: "id"')

#============================#
#Verifica se tem algum nome nulo no dataframe:
    if df['name'].isna().any():
        erros.append('Existe nome nulo em: "name"')

#============================#
#Verifica se tem algum id com duplicidade:
    if df['id'].duplicated().any():
        erros.append('Existe duplicidade em: "id"')

#============================#
#Verifica se as avaliações estão na faixa correta:
    if not df['rating'].dropna().between(0,100).all():
        erros.append('Existe avaliações incorretas em: "rating"')

#============================#
#Criando uma lista para utilizá-la no FOR para analisar se existe 
#algum registro por coluna com dados negativos

    colunas_negativas = [
        'review_count',
        'people_polled',
        'main_hours',
        'extra_hours',
        'completionist_hours'
    ]

    for coluna in colunas_negativas:
        if (df[coluna].dropna() < 0).any():
            erros.append(f'Existe números negativos em: {coluna}')

#============================#
#Retorna a lista com todos os erros do dataframe ;)
    return erros

#============================#

