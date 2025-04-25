FIAP - Faculdade de Informática e Administração Paulista


##Nome do projeto:  Cap 6 - Python e além
##Nome do grupo: Grupo 9

##Integrantes: * Fátima Vilela Candal – RM563003

##Professores:
##Tutor(a)
* Leonardo Ruiz Orabona
##Coordenador(a)
* André Godoi Chiovato

##Descrição
A atividade acadêmica trata das informações fornecidas sobre agrotechs e a colheita de cana-de-açúcar. Escolhi atuar na área de “Gestão Agrícola” do agronegócio. 
Efetuei uma conexão com o arquivo excel “tabela6588.xlsx” e após, criei gráficos para gerenciar dados de produção agrícola da cana-de-açúcar, como quantidade colhida, perdas, área plantada, área colhida, produção e rendimento médio.

##Estrutura de pastas
Os arquivos estão GITHUB no caminho:
https://github.com/rm563003/FIAP/tree/main/FASE%202%20-%20CAP%206/Repository

*FIAP/FASE 2 – CAP 6/Repository/

* assets: Imagens geradas na execução do código fonte.
area_colhida.png
area_plantada.png
produção.png
rendimento médio.png

* document: Documentos do projeto. 
Cap 6 - Python e além.docx
       ** other: TemplateConexaoBanco.py

* src: Código fonte criado e arquivo excel.
AreaColhida.py
AreaPlantada.py
ProducaoToneladas.py
RendimentoMedio.py
tabela6588.xlsx 

* README.md

##Como executar o código
Criar no drive “C:/” a pasta “FIAP” e copiar o arquivo excel “tabela6588.xlsx” para a pasta criada ("C:/FIAP/tabela6588.xlsx") e após, executar no “PYCHARM” os códigos que estão no repositório na pasta “src (/Repository/src)”.

Para executar o código instalar e importar as bibliotecas:
#install package matplotlib
#install package pandas

import matplotlib.pyplot as plt
import pandas as pd



##Arquivo Excel “tabela6588”
Tabela 6588 - Série histórica da estimativa anual da área plantada, área colhida, produção e rendimento médio dos produtos das lavouras de cana de açúcar.

Fonte: IBGE – Levantamento Sistemático da Produção Agrícola
Os dados são uma atualização mensal a estimativa para a safra COMPLETA, anual. Não é uma estimativa para a produção mensal.

Unidade da Federação – Pernambuco
Produto das lavouras – 11 Cana-de-açúcar 
