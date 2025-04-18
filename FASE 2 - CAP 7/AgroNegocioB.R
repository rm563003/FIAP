
# FatimaCandal_RM563003_fase2_cap7

#instalacao de pacote 
#install.packages("readxl") 

#comando setwd, determina um diretorio de trabalho.
setwd("C:/FIAP") 

# Carregar os dados (se ainda não estiverem carregados)
library(readxl)
dados <- read_excel("agro.xlsx")

# Escolher a variável qualitativa nominal: Tipo de Cultivo
tipo_cultivo <- dados$`Tipo de Cultivo`

# Criar tabela de frequência
tabela_frequencia <- table(tipo_cultivo)

# Análise Gráfica: Gráfico de Barras
barplot(tabela_frequencia, main = "Distribuição de Tipos de Cultivo",
        xlab = "Tipo de Cultivo", ylab = "Frequência", col = rainbow(length(tabela_frequencia)))

# Adicionar rótulos com as frequências
text(x = 1:length(tabela_frequencia), y = tabela_frequencia + 1, labels = tabela_frequencia, pos = 3)

# Escolher a variável qualitativa ordinal: Nível de Tecnologia
nivel_tecnologia <- factor(dados$`Nível de Tecnologia`, levels = c("Baixo", "Médio", "Alto"), ordered = TRUE)

# Criar tabela de frequência
tabela_frequencia_tec <- table(nivel_tecnologia)

# Análise Gráfica: Gráfico de Barras (ordenado)
barplot(tabela_frequencia_tec, main = "Distribuição de Níveis de Tecnologia",
        xlab = "Nível de Tecnologia", ylab = "Frequência", col = c("lightcoral", "lightskyblue", "lightsalmon"))

# Adicionar rótulos com as frequências
text(x = 1:length(tabela_frequencia_tec), y = tabela_frequencia_tec + 1, labels = tabela_frequencia_tec, pos = 3)
