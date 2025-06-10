Projeto de Pluviômetro Digital com ESP32
Este projeto integra um sensor ultrassônico HC-SR04 com um ESP32 para medir o volume de chuva acumulada em um recipiente cilíndrico. Os dados são processados em tempo real e exibidos via monitor serial, simulando um sistema de coleta pluviométrica.

Objetivos da Fase
Medir a altura da água de chuva em um reservatório usando sensor ultrassônico.

Calcular a precipitação acumulada em milímetros (mm).

Registrar e somar o volume diário de chuva.

Fornecer um botão físico para ativar manualmente a medição (simulação da rotina diária).

Exibir os resultados de forma clara no terminal serial do ESP32.

Componentes Utilizados
ESP32

Sensor Ultrassônico (HC-SR04 ou compatível)

Botão físico (com pull-down interno)

Recipiente cilíndrico (definido no código como 50 cm de altura e 20 cm de diâmetro)

 Justificativa da Estrutura de Cálculo
A altura da água é obtida subtraindo a distância medida até a superfície da água da altura total do recipiente.

O volume de água é calculado pela fórmula geométrica de volume de um cilindro:

𝑉=𝜋⋅𝑟^2⋅ℎ 

Onde r é o raio e h é a altura da coluna d'água.

O volume (em cm³) é convertido em mm de precipitação com base na equivalência hidrológica:

1 mm de chuva equivale a 1 litro/m².

O volume é dividido pela área da seção do recipiente (convertida para m²) para obter a precipitação em mm.

Como Funciona
Ciclo Principal (loop())
O código aguarda o pressionamento de um botão conectado ao pino 17.

Quando o botão é pressionado:

É iniciada uma medição.

A distância até a superfície da água é medida com 5 leituras e média filtrada.

A altura da água é usada para calcular a precipitação.

O valor é somado ao total acumulado de chuva.

Os dados são exibidos no terminal serial.

🔎 Medição (measureDistance())
Envia pulsos de trigger e mede o tempo de retorno do eco.

Converte o tempo em distância usando a velocidade do som.

Realiza várias leituras e filtra valores fora do intervalo esperado (ex: ruídos ou valores inválidos).

Retorna a média das distâncias válidas.

💧 Conversão para Precipitação (distanceToRainfall())
Calcula a altura da água no recipiente.

Determina o volume em cm³ (com base no diâmetro do recipiente).

Converte o volume para mm de chuva com base na área de captação.