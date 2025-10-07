<style>
</style>

## Projeto FarmTech Solutions – Visão Computacional com YOLOv5 e CNN do zero

## 📁 **Sobre o Projeto**

## 📌 Projeto FarmTech Solutions – Visão Computacional com YOLOv5v e CNN do zero

Este projeto demonstra as soluções desenvolvidas para as Entregas 1 e 2 do projeto da disciplina PBL Fase 6 da FIAP, aplicando técnicas de Visão Computacional com YOLOv5 e CNN do zero, com foco em dois objetos distintos: **cat** e **bike**. O objetivo é treinar um modelo capaz de identificar esses objetos com alta acurácia, validando seu uso em cenários reais da FarmTech Solutions. 

<style>
</style>

## 📌 Descrição do Projeto

A FarmTech Solutions está expandindo seus serviços de inteligência artificial
para além do agronegócio, atuando agora nas áreas de saúde animal, segurança
patrimonial, controle de acesso e análise de documentos. Como parte do time de
desenvolvedores, nosso objetivo foi demonstrar na prática o funcionamento de um
sistema de visão computacional utilizando YOLO, com foco em acurácia e
aplicabilidade.

           

## 📹 **Demonstração em Vídeo**

Assista ao vídeo com a explicação e funcionamento do
projeto: [YouTube – Não listado] (https://www.youtube.com/watch?v=SEU_LINK_AQUI)

            

## 📌 **Objetivo**

Demonstrar o uso de YOLOv5 e CNN do zero para detecção de objetos em imagens, com aplicação prática para clientes da FarmTech Solutions.

[FarmTechVision_Grupo7 - Google Drive]

https://drive.google.com/drive/folders/1e6rJrdMxQRRpNJW-nlHGcV0AqA_5cumV

[FIAP/FarmTechVision_Grupo7 at main · rm563003/FIAP · GitHub]

https://github.com/rm563003/FIAP/tree/main/FarmTechVision_Grupo7

            

## 🗂**️** **Estrutura do Repositório GITHUB**

Os arquivos estão no GITHUB:

https://github.com/rm563003/FIAP/tree/main/FarmTechVision_Grupo7

<img title="" src="Projeto.png" alt="">

<img title="" src="file:///G:/PARTICULAR/FIAP_IA/Fase 6 1009 até 1410/TRABALHO/DEEP/FarmTechVision_Grupo7/imagens/Projeto.png" alt="">

## 

### **🗂️ DATASET GOOGLE DRIVE**

O conjunto de dados foi organizado no Google Drive e contém:

-  **80 imagens no total**

-  40 imagens de gatos (cat)   

-  40 imagens de bicicletas (bike) - Separadas em:

-  32 para treino

-  4 para validação

-  4 para teste

-  Rotuladas com [Make Sense IA] (https://www.makesense.ai/) e salvas no formato YOLO.

🔗 Acesse o dataset completo no Google Drive:  

https://drive.google.com/drive/folders/1qkNb4RV7mHWI3fwiyvHKzPm7rb9KBSKN

/FarmTechVision_Grupo7/

  └── dataset/

      ├── images/

      │   ├── train/

      │   ├── val/

      │   └── test/

      └── labels/

          ├── train/

          ├── val/

          └── test/

# 



# 🔍 Entrega 2 –    Projeto FarmTech Solutions: Visão Computacional com YOLOv5 adaptável, YOLOv5 tradicional, CNN do zero

### Comparar o desempenho de três abordagens de Visão Computacional aplicadas à base personalizada criada na Entrega 1:

### 2. YOLO Adaptável — modelo treinado com base criada na Entrega 1

### 3. YOLO Padrão — modelo pré-treinado (sem customização)

### 4. CNN do Zero — rede neural convolucional construída manualmente

<style>
</style>

## 🔍 Entrega 2 – Comparação de Abordagens

## [entrega2_comparativo_fase6.ipynb - Colab]

https://colab.research.google.com/drive/1oIQeX-O1x54jBryk0rwJXX4GrAnyRiUH)

<style>
</style>

## 🔄 Abordagens implementadas:

## 2. YOLO Adaptável — modelo treinado com base criada na Entrega 1

### 3. YOLO Padrão — modelo pré-treinado (sem customização)

### 4. CNN do Zero — rede neural convolucional construída manualmente

<style>
</style>

## 📊 Comparativo de Métricas

<style> </style>

| Critério                       | YOLOv5s<br> Adaptável | YOLOv5s<br> Tradicional | CNN<br> do Zero |
| ------------------------------ | --------------------- | ----------------------- | --------------- |
| Precisão                       | 0.93                  | 0.78                    | 0.91            |
| Revocação                      | 1.00                  | 0.85                    | 0.88            |
| mAP@0.5                        | 0.995                 | 0.82                    | -----------     |
| Tempo<br> de treinamento (min) | 45                    | 0                       | 12              |
| Tempo<br> de inferência (s)    | 0.5                   | 0.2                     | 0.4             |
| Tipo<br> de saída              | Detecção              | Detecção                | Classificação   |

 

# 📈 Conclusões

<style>
</style>

### - YOLOv5s é ideal para aplicações com necessidade de localização precisa.

### - YOLOv5s é útil para testes rápidos e protótipos.

### - CNN é eficaz para classificação simples com baixo custo computacional.





# 👥 **Autores**

# Grupo 7 — FIAP

## •       Fátima Vilela Candal

## •       Gabriel Viel dos Santos Delfino

## •       Guilherme Campos Hermanowski

## •       Jonathan Willian Luft

## •       Matheus Alboredo Soares
