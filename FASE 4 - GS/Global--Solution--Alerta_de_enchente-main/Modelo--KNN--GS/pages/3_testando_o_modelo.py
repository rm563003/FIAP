# Imports
import pandas as pd
import numpy as np
import streamlit as st
from joblib import load
from sklearn.impute import SimpleImputer

# Título
st.title('🔬 Teste do Modelo KNN com Dados Aleatórios')
st.markdown('''
Vamos simular uma nova base com os mesmos padrões dos dados reais, e verificar como o modelo KNN treinado se comporta.
''')

# Carrega a base original para extrair estrutura
df_real = pd.read_csv("dados_externos\dados.csv")

# Remove a variável alvo (flood) da simulação
X_real = df_real.select_dtypes(include=[np.number]).drop('flood', axis=1)

# Limites das variáveis
minimos = X_real.min()
maximos = X_real.max()

# Tamanho da nova base aleatória
n_amostras = 50  # você pode ajustar esse valor

# Gera base aleatória com numpy dentro dos limites
dados_aleatorios = {
    coluna: np.random.uniform(low=minimos[coluna], high=maximos[coluna], size=n_amostras)
    for coluna in X_real.columns
}

df_aleatorio = pd.DataFrame(dados_aleatorios)
st.subheader("📊 Base Aleatória Gerada")
st.dataframe(df_aleatorio)

# Carregando modelo e pré-processadores
knn_model = load("modelo_ml/modelo_knn.pkl")
scaler = load("modelo_ml/scaler_knn.pkl")
imputer = load("modelo_ml/imputer_knn.pkl")

# Previsão com os dados aleatórios
X_imputado = imputer.transform(df_aleatorio)
X_escalado = scaler.transform(X_imputado)
y_pred = knn_model.predict(X_escalado)

# Mostrando resultados
st.subheader("🔎 Previsões do Modelo KNN")
df_resultado = df_aleatorio.copy()
df_resultado['Previsão'] = y_pred
st.dataframe(df_resultado)

# Contagem de classes previstas
st.subheader("📈 Distribuição das Classes Previstas")
st.bar_chart(df_resultado['Previsão'].value_counts())

# Conclusão do Projeto
st.header("📌 Conclusão")

st.markdown("""
Este projeto apresentou uma abordagem completa de classificação utilizando o algoritmo **K-Nearest Neighbors (KNN)**. O modelo foi escolhido com base em seu excelente desempenho em testes, alcançando uma acurácia próxima de 99%.

Além da construção do modelo, destacamos boas práticas como:
- **Tratamento de valores ausentes** com `SimpleImputer`;
- **Normalização dos dados** com `StandardScaler`;
- **Salvamento e reutilização** do modelo e dos pré-processadores com `joblib`;
- **Avaliação clara e objetiva** por meio de métricas e relatórios de desempenho;
- **Capacidade de aplicação prática**, inclusive em bases aleatórias ou externas.

Com isso, o sistema está pronto para ser integrado em aplicações reais, com confiança em sua capacidade de generalização e manutenção. Essa estrutura modular e reutilizável torna o modelo robusto e adaptável para diferentes conjuntos de dados e cenários.
""")




