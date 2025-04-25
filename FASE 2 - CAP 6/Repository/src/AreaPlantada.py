# FatimaCandal_RM563003_fase2_cap6

# Um sistema para gerenciar dados de produção agrícola, como como quantidade colhida,
# perdas, área plantada, área colhida, produção e rendimento médio.

# Levantamento Sistemático da Produção Agrícola - PE
# Estimativas para a safra de cana anual de Pernambuco

# Tabela 6588 - Série histórica da estimativa anual da área plantada, área colhida, produção e rendimento
# médio dos produtos das lavouras
# Unidade da Federação - Pernambuco
# Produto das lavouras - 11 Cana-de-açúcar

# Fonte: IBGE - Levantamento Sistemático da Produção Agrícola
# Os dados são uma atualização mensal da estimativa para a safra COMPLETA, anual.
# Não é uma estimativa para a produção mensal.


#install package matplotlib
#install package pandas

import matplotlib.pyplot as plt
import pandas as pd

# Load the Excel file
df = pd.read_excel("C:/FIAP/tabela6588.xlsx")

print(df.head())

# Generate a line plot for Área plantada (Hectares) over time
plt.figure(figsize=(10, 6))
plt.plot(df['Mês'], df['Área plantada (Hectares)'], marker='o')
plt.title('Área plantada (Hectares) ao longo do tempo')
plt.xlabel('Mês')
plt.ylabel('Área plantada (Hectares)')
plt.xticks(rotation=75)
plt.grid(True)
plt.tight_layout()
plt.savefig('area_plantada.png')
plt.show()

