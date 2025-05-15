import time

# Simulação de banco de dados SQL (lista de dicionários)
database = []

def inserir_dados(umidade, temperatura, ph, fosforo, potassio, bomba_status):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    database.append({
        'timestamp': timestamp,
        'umidade': umidade,
        'temperatura': temperatura,
        'ph': ph,
        'fosforo': fosforo,
        'potassio': potassio,
        'bomba_status': bomba_status
    })
    print("Dados inseridos com sucesso!")

def consultar_dados():
    print("\n--- Dados no Banco de Dados ---")
    for registro in database:
        print(registro)

def atualizar_dados(indice, nova_umidade):
    if 0 <= indice < len(database):
        database[indice]['umidade'] = nova_umidade
        print(f"Umidade do registro {indice} atualizada para {nova_umidade}")
    else:
        print("Índice inválido!")

def remover_dados(indice):
    if 0 <= indice < len(database):
        del database[indice]
        print(f"Registro {indice} removido!")
    else:
        print("Índice inválido!")

# Simulação de leitura do monitor serial e operações CRUD
print("Simulando leitura do monitor serial...")
inserir_dados(55.2, 28.5, 6.7, "Ausente", "Presente", "LIGADA")
inserir_dados(70.1, 29.1, 7.2, "Presente", "Ausente", "DESLIGADA")

consultar_dados()

atualizar_dados(0, 60.5)
consultar_dados()

remover_dados(1)
consultar_dados()
