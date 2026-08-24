# 🎮 PlayMyData ETL

> Pipeline de ETL de dados desenvolvido em Python e PostgreSQL para transformar dados brutos em informações prontas para análise.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)

## 📌 Sobre o Projeto

Este projeto surgiu com o intuito de aplicar na prática os conhecimentos adquiridos após o meu desenvolvimento da pipeline de ETL do Olist E-commerce. O objetivo desta versão inicial (V1) é construir uma pipeline funcional e sólida do dataset da PlayMyData, preparando o terreno para futuras análises sobre jogos de diferentes plataformas.

Durante o desenvolvimento, utilizei IA como apoio para acelerar a resolução de bugs, o que me ajudou a evoluir bastante de forma prática. Senti uma melhora significativa na minha fluência com ferramentas essenciais, como a navegação e operação no terminal Linux.

## 💾 Fonte de Dados

O projeto utiliza o [PlayMyData](https://zenodo.org/records/10262075), um dataset público de jogos estruturado com base em dados do **IGDB** e **HowLongToBeat**.

## 🏗️ Arquitetura do Pipeline

O processo segue a estrutura clássica de Extração, Transformação, Validação e Carga, conforme o fluxo abaixo:

```text
[ PlayMyData (CSV) ]
         |
         v
    [ Extract ]
         |
         v
   [ Transform ]
         |
         v
    [ Validate ]
         |
         v
      [ Load ]
         |
         v
   [ PostgreSQL ]
```

## 🛠️ Tecnologias Utilizadas

*   **Linguagem:** Python
*   **Manipulação de Dados:** Pandas, NumPy
*   **Banco de Dados:** PostgreSQL
*   **Integração com BD:** SQLAlchemy, psycopg2
*   **Ambiente e Versionamento:** python-dotenv, Git

## 🛡️ Regras de Qualidade (Validação)

Para garantir a integridade das informações antes da carga no banco de dados, o script de validação assegura que:

1. O DataFrame **não está vazio**.
2. Não existem **IDs nulos**.
3. Não existem **IDs duplicados**.
4. Não existem **nomes de jogos vazios**.
5. As **avaliações (ratings)** estão dentro da faixa correta (0 a 100).
6. Não existem **valores negativos** nas colunas de métricas e tempo: `review_count`, `people_polled`, `main_hours`, `completionist_hours`, `extra_hours`.

## 🚀 Como Executar

1. **Clone o repositório:**
```bash
   git clone https://github.com/thiagoferlopes/playmydata-games-etl.git
   cd playmydata-games-etl
```

2. **Crie e ative o ambiente virtual:**
```bash
   python3 -m venv .venv
   source .venv/bin/activate  # No Windows, use: .venv\Scripts\activate
```

3. **Instale as dependências:**
```bash
   pip install -r requirements.txt
```

4. **Configure o banco de dados PostgreSQL:**
   * Certifique-se de que o serviço do PostgreSQL está rodando.
   * Crie o banco e a tabela usando os scripts SQL do projeto:
```bash
     psql -U postgres -d postgres -f sql/create_database.sql
     psql -U postgres -d playmydata_etl -f sql/create_table.sql
```
   * **Nota:** o pipeline usa `to_sql(if_exists="replace")`, que recria a tabela automaticamente na primeira carga — inclusive sem a `PRIMARY KEY` definida no `create_table.sql`. Rodar esse script define a intenção original de schema, mas não é uma garantia permanente da estrutura após a primeira execução do pipeline.

5. **Configure as Variáveis de Ambiente:**
   * Crie um arquivo chamado `.env` na raiz do projeto e adicione as suas credenciais de acesso ao PostgreSQL, seguindo este formato:
```env
     DB_USER=seu_usuario
     DB_PASSWORD=sua_senha
     DB_HOST=localhost
     DB_PORT=5432
     DB_NAME=playmydata_etl
```

6. **Rode a pipeline:**
```bash
   python3 src/main.py
```

## 🧠 O que eu aprendi

Este projeto foi um excelente laboratório de testes e me trouxe aprendizados valiosos:

* **A importância da validação:** Percebi na prática por que validar os dados antes da etapa de *Load* é crucial para evitar falhas no banco. Aprendi a estruturar uma etapa de validação sólida em Python.
* **Desafios de Carga (Load):** Melhorei meus conhecimentos em extração e transformação, mas o carregamento via Pandas/SQLAlchemy foi um desafio. Descobri que o `to_sql(if_exists="replace")` recria a tabela do zero a cada carga, sem preservar a `PRIMARY KEY` definida manualmente no `create_table.sql`. Isso ficou evidente quando testei o `append`: sem a chave primária, o PostgreSQL não tinha como impedir a duplicação de registros, e rodar a pipeline duas vezes simplesmente empilhou os dados. Entender essa diferença entre o schema que eu desenhei e o schema que o Pandas realmente cria foi um dos aprendizados mais importantes do projeto.
* **Atenção aos detalhes dos dados:** Cometi o erro inicial de supor que a faixa de avaliações era 0-10, quando na verdade era 0-100. Isso me ensinou a sempre validar suposições contra o dado real (`describe()`, `min()`, `max()`) antes de codificar regras.
* **Evolução no Git:** Tive muito mais facilidade e confiança no uso do Git, resultado direto da constância e prática diária.