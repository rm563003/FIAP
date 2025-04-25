FIAP - Faculdade de Inform�tica e Administra��o Paulista


##Nome do projeto:  Cap 6 - Python e al�m
##Nome do grupo: Grupo 9

##Integrantes: * F�tima Vilela Candal � RM563003

##Professores:
##Tutor(a)
* Leonardo Ruiz Orabona
##Coordenador(a)
* Andr� Godoi Chiovato

##Descri��o
A atividade acad�mica trata das informa��es fornecidas sobre agrotechs e a colheita de cana-de-a��car. Escolhi atuar na �rea de �Gest�o Agr�cola� do agroneg�cio. 
Efetuei uma conex�o com o arquivo excel �tabela6588.xlsx� e ap�s, criei gr�ficos para gerenciar dados de produ��o agr�cola da cana-de-a��car, como quantidade colhida, perdas, �rea plantada, �rea colhida, produ��o e rendimento m�dio.

##Estrutura de pastas
Os arquivos est�o GITHUB no caminho:
https://github.com/rm563003/FIAP/tree/main/FASE%202%20-%20CAP%206/Repository

*FIAP/FASE 2 � CAP 6/Repository/

* assets: Imagens geradas na execu��o do c�digo fonte.
area_colhida.png
area_plantada.png
produ��o.png
rendimento m�dio.png

* document: Documentos do projeto. 
Cap 6 - Python e al�m.docx
       ** other: TemplateConexaoBanco.py

* src: C�digo fonte criado e arquivo excel.
AreaColhida.py
AreaPlantada.py
ProducaoToneladas.py
RendimentoMedio.py
tabela6588.xlsx 

* README.md

##Como executar o c�digo
Criar no drive �C:/� a pasta �FIAP� e copiar o arquivo excel �tabela6588.xlsx� para a pasta criada ("C:/FIAP/tabela6588.xlsx") e ap�s, executar no �PYCHARM� os c�digos que est�o no reposit�rio na pasta �src (/Repository/src)�.

Para executar o c�digo instalar e importar as bibliotecas:
#install package matplotlib
#install package pandas

import matplotlib.pyplot as plt
import pandas as pd



##Arquivo Excel �tabela6588�
Tabela 6588 - S�rie hist�rica da estimativa anual da �rea plantada, �rea colhida, produ��o e rendimento m�dio dos produtos das lavouras de cana de a��car.

Fonte: IBGE � Levantamento Sistem�tico da Produ��o Agr�cola
Os dados s�o uma atualiza��o mensal a estimativa para a safra COMPLETA, anual. N�o � uma estimativa para a produ��o mensal.

Unidade da Federa��o � Pernambuco
Produto das lavouras � 11 Cana-de-a��car 
