# FatimaCandal_RM563003_fase2_cap6

# Conexão para recuperar dados agrícolas de um banco de dados Oracle.
# Segue um template para a conexão com o banco de dados oracle:


import cx_Oracle

def conectar_banco():
    # Função para conectar ao banco de dados Oracle
    dsn_tns = cx_Oracle.makedsn('hostname', 'port', service_name='service_name')
    conn = cx_Oracle.connect(user='username', password='password', dsn=dsn_tns)
    return conn

def recuperar_dados(conn):
    # Função para recuperar dados do banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dados_agricolas")
    for row in cursor:
        print(row)
    cursor.close()

# Exemplo de uso
conn = conectar_banco()
recuperar_dados(conn)
conn.close()




