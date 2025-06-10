# Aqui importamos todas as bibliotecas e exibimos o DataFrame

# Imports

# Silenciando mensagens de aviso
import warnings
warnings.filterwarnings('ignore')

# importando bibliotecas para tratar, limpar e classificar os dados
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
import streamlit as st

# Configurações para melhorar a visualização
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('viridis')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

# Para reprodutibilidade
np.random.seed(42)

# Carregando o DataFrame
df = pd.read_csv("dados_externos\dados.csv")

# Exibindo a escala do Data Frame para uma melhor noção da quantidade de dados presentes nele
print(f"A escala do DataFrame é de {df.shape}\n")

print("Exibindo 10 linhas aleatórias para termos uma noção de como está o DataFrame:\n")
print(df.sample(10))

# Verificando informações gerais do DataFrame
print(f"Informações do DataFrame:")
print(df.info())

# Estatísticas descritivas do DataFrame
print("\n\nEstatísticas descritivas:\n\n")
print(df.describe())

# Contando quantas vezes cada cultura se repete
print("Contagem de cada tipo de cultura:")
print(df['flood'].value_counts())

# Configurações gerais
st.set_page_config(page_title='Análise de Dados', layout='wide')
# Título do aplicativo
st.title('Exploração de Dados')
# ================================================
# 1. Carregar os Dados
# ================================================
st.header('1. Carregar os Dados')
# Carregar os dados gerados
# Mostrar os primeiros registros
st.subheader('Visualização dos Dados')
st.dataframe(df.head())

# ================================================
# 2. Visão Geral dos Dados
# ================================================
st.header('2. Visão Geral dos Dados')
# Informações sobre o DataFrame
st.subheader('Informações do DataFrame')
st.write('Dimensões do DataFrame:')
st.write(f'Linhas: {df.shape[0]}, Colunas: {df.shape[1]}')
st.subheader('Tipos de Dados')
# Converter os tipos de dados para string
df_types = pd.DataFrame({
    'Coluna': df.columns,
    'Tipos de Dados': df.dtypes.astype(str)
})
st.write(df_types)
# Verificar valores ausentes
st.subheader('Valores Ausentes')
st.write(df.isnull().sum())
st.write("A base não possui valores ausentes!")
# Estatísticas Descritivas
st.subheader('Estatísticas Descritivas')
st.write(df.describe())