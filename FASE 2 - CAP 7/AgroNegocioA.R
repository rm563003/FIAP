
# FatimaCandal_RM563003_fase2_cap7

#instalacao de pacote 
#install.packages("readxl") 


#comando setwd, determina um diretorio de trabalho.
setwd("C:/FIAP") 

# Carregar os dados (caminho do arquivo Excel)
library(readxl)
dados <- read_excel("agro.xlsx")

# Escolher a variável quantitativa contínua: Área Plantada (hectares)
area_plantada <- dados$`Área Plantada (hectares)`

# Medidas de Tendência Central
media_area <- mean(area_plantada)
mediana_area <- median(area_plantada)
moda_area <- names(sort(table(area_plantada), decreasing = TRUE)[1]) # Aproximação da moda para contínuas

cat("Medidas de Tendência Central para Área Plantada (hectares):\n")
cat("Média:", media_area, "\n")
cat("Mediana:", mediana_area, "\n")
cat("Moda (aproximada):", moda_area, "\n\n")

# Medidas de Dispersão
desvio_padrao_area <- sd(area_plantada)
variancia_area <- var(area_plantada)
amplitude_area <- max(area_plantada) - min(area_plantada)
iqr_area <- IQR(area_plantada)

cat("Medidas de Dispersão para Área Plantada (hectares):\n")
cat("Desvio Padrão:", desvio_padrao_area, "\n")
cat("Variância:", variancia_area, "\n")
cat("Amplitude:", amplitude_area, "\n")
cat("Intervalo Interquartil (IQR):", iqr_area, "\n\n")

# Medidas Separatrizes
quartis_area <- quantile(area_plantada, probs = c(0.25, 0.5, 0.75))
percentis_area <- quantile(area_plantada, probs = c(0.10, 0.50, 0.90))

cat("Medidas Separatrizes para Área Plantada (hectares):\n")
cat("Quartis:\n")
print(quartis_area)
cat("\nPercentis (10%, 50%, 90%):\n")
print(percentis_area)
cat("\n")

# Análise Gráfica
hist(area_plantada, main = "Histograma da Área Plantada (hectares)",
     xlab = "Área Plantada (hectares)", ylab = "Frequência", col = "lightblue")

boxplot(area_plantada, main = "Boxplot da Área Plantada (hectares)",
        ylab = "Área Plantada (hectares)", col = "lightgreen")

# Adicionar uma linha para a média no histograma
abline(v = media_area, col = "red", lty = "dashed", lwd = 2)
legend("topright", legend = paste("Média =", round(media_area, 2)),
       col = "red", lty = "dashed", lwd = 2)
