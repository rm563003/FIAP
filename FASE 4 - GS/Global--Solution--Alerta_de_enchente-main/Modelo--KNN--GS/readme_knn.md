## Escopo Geral

Este projeto de machine learning tem como objetivo classificar a ocorrência de inundações com base em variáveis ambientais e urbanas. Após testes com múltiplos algoritmos, o modelo K-Nearest Neighbors (KNN) foi escolhido por apresentar alta acurácia e bom desempenho geral.
Nosso treinamento foi feito com base em um arquivo csv extraido de nosso banco de dados SQL que foi alimentado com a base de dados do https://bdmep.inmet.gov.br.

## 📌 Funcionalidades
- Pré-processamento completo (imputação e normalização);

- Treinamento e avaliação de múltiplos modelos (Random Forest, SVM, KNN);

- Armazenamento do modelo final e pré-processadores com joblib;

- Criação de base de dados sintética com NumPy;

- Interface interativa com Streamlit para visualização e testes;

- Reutilização do modelo KNN com novas bases de dados.

## 🚀 Tecnologias Utilizadas
- Python 3.10+

- scikit-learn

- pandas, numpy

- matplotlib, seaborn

- imbalanced-learn

- joblib

- streamlit

## 📁 Estrutura do Projeto
bash
Copiar
Editar
projeto/
│
├── modelo/
│   ├── knn_model.joblib        # Modelo KNN treinado
│   ├── scaler.joblib           # Normalizador (StandardScaler)
│   ├── imputer.joblib          # Imputador de dados faltantes
│
├── pages/
│   └── 3_testando_o_modelo.py  # Página Streamlit para teste final
│
├── dados/
│   └── dados.csv               # Base original de treino
│   └── dataset.csv             # Base externa (nova) para predição
│
├── gerar_dados_sinteticos.py   # Gera dataset com NumPy baseado na estrutura original
├── treinar_modelo_knn.py       # Script para treinar e salvar modelo KNN
├── app.py                      # App principal do Streamlit
├── README.md                   # Este arquivo

## ⚙️ Etapas do Projeto
### - 1. Treinamento do Modelo
O script treinar_modelo_knn.py realiza:

Carregamento e tratamento dos dados;

Divisão em treino/teste;

Treinamento dos modelos;

Armazenamento do melhor modelo (KNN) e pré-processadores.

### - 2. Criação de Dados Sintéticos
gerar_dados_sinteticos.py usa a estrutura e os limites da base real (dados.csv) para gerar uma nova base com NumPy, útil para testes e validação.

### - 3. Interface de Testes com Streamlit
A página pages/3_testando_o_modelo.py:

Carrega o modelo e os transformadores salvos;

Permite testar o modelo com novos dados (inclusive sintéticos);

Mostra métricas de desempenho em tempo real.

## - 🧠 Como Rodar o Projeto
### - 1. Instale as dependências:
bash
Copiar
Editar
pip install -r requirements.txt
### - 2. Treine o modelo:
bash
Copiar
Editar
python treinar_modelo_knn.py
### - 3. Gere dados sintéticos (opcional):
bash
Copiar
Editar
python gerar_dados_sinteticos.py
### - 4. Rode o Streamlit:
bash
Copiar
Editar
streamlit run app.py
## ✅ Resultados
O modelo KNN apresentou desempenho superior aos demais algoritmos testados, com destaque para:

Acurácia: ~99%

Alta capacidade de generalização

Baixa complexidade computacional

## 📌 Conclusão
O projeto entrega uma solução completa e funcional de classificação, com foco em modularidade, reuso e aplicabilidade prática. O uso de joblib para persistência e a integração com Streamlit tornam a ferramenta robusta e acessível para usuários técnicos e não técnicos.

