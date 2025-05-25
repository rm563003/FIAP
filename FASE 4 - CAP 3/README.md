# Implementando algoritmos de Machine Learning com Scikit-learn

# FIAP - Inteligência artificial e data science

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

## Nome do grupo XX

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Fátima Viela Candal </a>
- <a href="https://www.linkedin.com/company/inova-fusca">Guilherme Campos Hermanowski </a>
- <a href="https://www.linkedin.com/company/inova-fusca">Gabriel Viel </a>
- <a href="https://www.linkedin.com/company/inova-fusca">Jonathan Willian Luft </a>
- <a href="https://www.linkedin.com/company/inova-fusca">Matheus Alboredo Soares</a> 


## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">ANDRÉ GODOI CHIOVATO</a>


# Projeto Implementando algoritmos de Machine Learning com Scikit-learn

Este projeto visa a classificação de variedades de grãos de trigo com base em suas características físicas, seguindo a metodologia CRISP-DM. O processo envolve um conjunto de tarefas bem detalhadas, incluindo análise exploratória dos dados, pré-processamento, implementação de algoritmos de classificação, otimização de modelos e interpretação dos resultados.

---

## 📁 Estrutura de pastas

Os arquivos estão GITHUB no caminho: https://github.com/rm563003/FIAP/tree/main/FASE%204%20-%20CAP%203

FIAP /FASE 4 - CAP 3/

- IMAGES:CORRELACAO.png,HISTOGRAMA.png, SEPARABILIDADE DAS CLASSES.PNG, VARIAVEIS_RANDON_FOREST.png  
- FASE4_SEEDS.ipynb: Código em Python.  
- seeds_dataset.txt: Dataset.

---

## ⚙️ DATASET

Os dados utilizados (seeds_dataset.txt) são provenientes do Seeds Dataset do UCI Machine Learning Repository, que contém medições de 210 amostras de grãos de trigo, divididas em três variedades: Kama, Rosa e Canadian. Os atributos analisados incluem área, perímetro, compacidade, comprimento do núcleo e coeficiente de assimetria, entre outros.

Para iniciar o estudo, os dados (seeds_dataset.txt) devem ser carregados em um ambiente de análise como Google Colab, permitindo a exploração da estrutura, a identificação de padrões e a preparação dos dados para modelagem.

O conjunto de dados é bem estruturado e adequado para análises de Machine Learning. Ele contém três variedades de sementes e diversas características físicas que podem ser usadas para classificá-las. 

## 🧠 Análise dos resultados dos modelos de classificação 

🔹 Melhor desempenho geral: Random Forest
•	Alta acurácia (92,06%), precisão e revocação equilibradas.
•	Melhor AUC-ROC (98,30%), indicando excelente distinção entre classes.
•	Menor Log Loss (0,2246), o que significa que as previsões do modelo são confiáveis.

🔹 Bom desempenho: KNN e Regressão Logística
•	O KNN tem boa acurácia (87,30%) e AUC-ROC (94,97%), mas seu Log Loss (1,8758) é elevado, sugerindo previsões menos confiáveis.
•	A Regressão Logística tem acurácia similar à SVM, mas com AUC-ROC alto (97,66%), o que indica bom poder de discriminação.

🔹 Desempenho intermediário: SVM e Naive Bayes
•	SVM apresenta acurácia de 85,71%, mas sem valores de AUC-ROC e Log Loss, dificultando uma avaliação completa.
•	Naive Bayes tem a menor acurácia (82,54%) e um Log Loss maior (0,8231), o que pode indicar previsões menos certeiras.

🔹 Conclusão e recomendações
✅ Random Forest parece ser a melhor escolha para essa tarefa, pois equilibra bem todas as métricas.
✅ Se a interpretabilidade for importante, Regressão Logística pode ser uma opção sólida.
✅ Se quiser reduzir o custo computacional, KNN pode ser útil, mas pode sofrer com previsões menos confiáveis.
✅ SVM e Naive Bayes podem ser úteis dependendo da natureza dos dados, mas parecem menos eficazes aqui.

---

=====================================================================================================================
```

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
