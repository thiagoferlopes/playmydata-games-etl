def validate(df):
    erros = []

    if df.empty is True:
       erros.append('DataFrame vazio')

    if df['id'].isna().any() != 0:
        erros.append('Existe item nulo em: "id"')

    if df['id'].duplicated().any() != 0:
        erros.append('Existe duplicidade em: "id"')

    if not df['rating'].dropna().between(0,100).all():
        erros.append('Existe avaliações incorretas em: "rating"')

    colunas_negativas = [
        'review_count',
        'people_polled',
        'main_hours',
        'extra_hours',
        'completionist_hours'
    ]

    for coluna in  colunas_negativas:
        if (df[coluna].dropna() < 0).any():
            erros.append(f'Existe números negativos em: {coluna}')
            
    return erros