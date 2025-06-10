import streamlit as st

st.set_page_config(
    page_title='Análise de Dados Pluviométricos',
    page_icon=':umbrella_with_rain_drops:',
    layout='wide'
)
st.title('Análise de Dados Pluviométricos :umbrella_with_rain_drops:')
st.write('Bem-vindo ao aplicativo de análise de dados pluviométricos.')
st.markdown("""
Esta aplicação se utiliza de análise de dados pluviométricos de diversas regiões para, por meio de sistemas de ML KNN, fazer predições e gerar alertas de risco de enchente para regiões que se encaixem nos padrões de risco.
""")
