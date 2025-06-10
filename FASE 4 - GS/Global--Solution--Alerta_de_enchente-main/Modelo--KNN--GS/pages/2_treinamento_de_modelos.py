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
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestRegressor
import streamlit as st
from sklearn.impute import SimpleImputer
import joblib


# Configurações para melhorar a visualização
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('viridis')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

# Para reprodutibilidade
np.random.seed(42)

# Carregando o DataFrame
df = pd.read_csv("dados_externos\dados.csv")

# Preparando os dados para modelagem

# Selecionar só colunas numéricas antes do split para manter alinhamento
X = df.select_dtypes(include=[np.number]).drop('flood', axis=1)
y = df['flood']

# Dividir treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Normalizar
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Treinar Random Forest
from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(random_state=42, n_estimators=100, class_weight='balanced')
rf_model.fit(X_train_scaled, y_train)

y_pred_rf = rf_model.predict(X_test_scaled)

st.header('Treinando o Modelo de Machine Learning')
st.markdown('''Aqui nós vamos treinar alguns modelos de machine learning para que, com base em seus desempenhos, possamos selecionar o modelo que mais se destaca positivamente para atuar em nossa aplicação.\n''')

st.markdown('''Iremos fazer os testes com 3 diferentes tipos de modelos de Machine Learning.''')
st.markdown("""
## 🤖 Tipos de Modelo de Machine Learning

- **Random Forest**
  - Conjunto de árvores de decisão para melhorar a precisão.
- **K-Nearest Neighbors (KNN)**
  - Classifica com base na proximidade dos vizinhos mais próximos.
- **Máquinas de Vetores de Suporte (SVM)**
  - Encontra o hiperplano ótimo para separar classes.
""")

st.subheader('Random Forest')


# st.write(f'**Acurácia do modelo (R² no conjunto de teste):** {accuracy_score(y_test, y_pred_rf):.4f}')
# st.write(classification_report(y_test, y_pred_rf))

from sklearn.metrics import accuracy_score, classification_report, r2_score
import pandas as pd

accuracy_rf = accuracy_score(y_test, y_pred_rf)
r2 = r2_score(y_test, y_pred_rf)

# Métricas principais
col1, col2 = st.columns(2)
col1.metric("✅ Acurácia", f"{accuracy_rf:.4f}")
col2.metric("📈 R²", f"{r2:.4f}")

# Relatório de Classificação
report_dict = classification_report(y_test, y_pred_rf, output_dict=True)
report_df = pd.DataFrame(report_dict).transpose()

st.subheader("📋 Relatório de Classificação")
st.dataframe(report_df.style.format("{:.2f}"))


st.subheader('KNN')

# Imputar valores ausentes
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.3, random_state=42)

# Normalizar
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Treino
knn_model = KNeighborsClassifier(n_neighbors=25)
knn_model.fit(X_train_scaled, y_train)

joblib.dump(knn_model, 'modelo_knn.pkl')
joblib.dump(scaler, 'scaler_knn.pkl')
joblib.dump(imputer, 'imputer_knn.pkl')

# Previsões
y_pred = knn_model.predict(X_test_scaled)

# Cálculo da acurácia
accuracy_knn = accuracy_score(y_test, y_pred)

# Mostra a acurácia com destaque
st.subheader("✅ Acurácia do Modelo KNN")
st.metric(label="🎯 Acurácia", value=f"{accuracy_knn:.4f}")

# Gera o relatório de classificação
report_dict = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report_dict).transpose()

# Exibe o relatório como tabela interativa
st.subheader("📋 Relatório de Classificação")
st.dataframe(report_df.style.format("{:.2f}"))

st.subheader('SVM')

# Treinando o modelo SVM
svm_model = SVC(kernel='rbf', random_state=42)
svm_model.fit(X_train_scaled, y_train)

# Fazendo previsões
y_pred_svm = svm_model.predict(X_test_scaled)


# Avaliação do modelo SVM
svm_accuracy = accuracy_score(y_test, y_pred_svm)
report_dict = classification_report(y_test, y_pred_svm, output_dict=True)
report_df = pd.DataFrame(report_dict).transpose()
cm = confusion_matrix(y_test, y_pred_svm)

# Seção visual no Streamlit
st.header("🧠 Avaliação do Modelo SVM")

# Métricas principais
col1, col2 = st.columns(2)
col1.metric(label="🎯 Acurácia", value=f"{svm_accuracy:.4f}")
col2.metric(label="📌 Kernel", value="RBF")

# Relatório de Classificação
st.subheader("📋 Relatório de Classificação")
st.dataframe(report_df.style.format("{:.2f}"))

# Matriz de Confusão
st.subheader("🧩 Matriz de Confusão")
fig, ax = plt.subplots()
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
ax.set_xlabel("Classe Predita")
ax.set_ylabel("Classe Real")
ax.set_title("Matriz de Confusão - SVM")
st.pyplot(fig)

# importando o ML escolhido para um joblib para que seja utilizado posteriormente

from joblib import dump

# ... (seu código existente até a parte do KNN)

# Treina e avalia
knn_model = KNeighborsClassifier(n_neighbors=25)
knn_model.fit(X_train_scaled, y_train)

# Salva o modelo treinado e o scaler
dump(knn_model, 'knn_model.joblib')
dump(scaler, 'scaler.joblib')  # É importante salvar o scaler também para pré-processar novos dados
dump(imputer, 'imputer.joblib')  # Salva o imputer para tratar valores ausentes

# ... (restante do seu código)