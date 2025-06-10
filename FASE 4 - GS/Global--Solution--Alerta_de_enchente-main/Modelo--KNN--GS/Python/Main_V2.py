import pandas as pd
from datetime import datetime
import pyodbc
import os

# Lendo o CSV na pasta Dados Externo e armazenando no DF.
df = pd.read_csv("Dados_Externo\Dados_INMET_2022_2024_SP_V2.csv")
    
#Padronizando as colunas
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

#Tratando a coluna DataHora para DATETIME no SQL SERVER
df["datahora"] = pd.to_datetime(df["datahora"], errors="coerce")

#Ajusta valores vazios
df = df.ffill()
df = df.where(pd.notnull(df), None)

#Nomeando a tabela no SQL_SERVER:
nome_tabela = "LogHistorico_INMET"


#String de Conexão com SQL SERVER LOCAL.
conexao = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=192.168.0.11,1433;"
    "DATABASE=Meteorologia;"
    "UID=pyUser;"
    "PWD=1234;"
)
cursor = conexao.cursor()

#Tratando os tipos de dados a fim de eficiencia no banco de dados.
colunas_sql = []
for col in df.columns:
    if col == "datahora":
        colunas_sql.append(f"[{col}] DATETIME")
    elif df[col].dtype in ["float64", "int64"]:
        colunas_sql.append(f"[{col}] FLOAT")
    else:
        colunas_sql.append(f"[{col}] VARCHAR(100)")

#Cria dinâmicamente a tabela com os dados do CSV importado, automatizando o script SQL de declaração das colunas da tabela e também de valores.
sql_create = f"""
IF OBJECT_ID('{nome_tabela}', 'U') IS NOT NULL
    DROP TABLE {nome_tabela};

CREATE TABLE {nome_tabela} (
    Id_Registro INT IDENTITY(1,1) PRIMARY KEY,
    {', '.join(colunas_sql)}
)
"""
cursor.execute(sql_create)
conexao.commit()


#Inserindo os Dados no SQL Server
colunas = ", ".join(f"[{col}]" for col in df.columns)
placeholders = ", ".join("?" for _ in df.columns)
sql_insert = f"INSERT INTO {nome_tabela} ({colunas}) VALUES ({placeholders})"

for _, row in df.iterrows():
    cursor.execute(sql_insert, tuple(row))

conexao.commit()

#Output de finalização de inserção no banco de dados.
print(f"Inserção concluída: {len(df)} registros na tabela {nome_tabela}.")

#Consulta do SQLServer para Exportar para CSV para o ML
query = f"SELECT * FROM {nome_tabela}"
df = pd.read_sql(query, conexao)

#Nome do arquivo:
dt_log = datetime.now().strftime("%Y_%m_%d_%H%M%S")
nome_arquivo = f"{nome_tabela}_exportado_{dt_log}.csv"

#Pasta do Script
caminho_script = os.path.abspath(os.path.dirname(__file__))

#Pasta do Caminho que tem que salvar, com validação (DADOS_ML)
pasta_destino = os.path.join(caminho_script, "..", "Dados_ML")
os.makedirs(pasta_destino, exist_ok=True)

#Caminho do Csv para exportar
caminho_csv = os.path.join(pasta_destino, nome_arquivo)

#Exportando
df.to_csv(caminho_csv, index=False, encoding="utf-8")
print(f"Exportado com sucesso para: {caminho_csv}")