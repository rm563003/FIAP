#include <Arduino.h>

// Definicoes dos pinos
const int TRIG_PIN = 5;       // Pino Trigger do sensor
const int ECHO_PIN = 18;      // Pino Echo do sensor
const int BUTTON_PIN = 17;    // Pino do botão

// Constantes do pluviômetro
const float SOUND_SPEED = 0.0343; // Velocidade do som em cm/us
const int NUM_READINGS = 5;       // Número de leituras para média
const int READING_DELAY = 50;     // Delay entre leituras (ms)
const int TIMEOUT_US = 30000;     // Timeout de 30ms (~5m)
const float TANK_HEIGHT = 50.0;   // Altura total do recipiente (cm)
const float TANK_DIAMETER = 20.0; // Diâmetro do recipiente (cm)

// Variáveis globais
float lastRainfall = 0.0;         // Última medição de chuva (mm)
float totalRainfall = 0.0;         // Acumulado de chuva (mm)
unsigned long lastMeasureTime = 0; // Timestamp da última medição

void setup() {
  Serial.begin(115200);
  
  // Configura pinos
  pinMode(BUTTON_PIN, INPUT_PULLDOWN); // Botão com pull-down
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  
  // Inicialização segura do sensor
  digitalWrite(TRIG_PIN, LOW);
  
  // Aguarda estabilização
  delay(1000);
  
  Serial.println("\n===== PLUVIOMETRO DIGITAL =====");
  Serial.println("Pressione o botao para medir a chuva acumulada");
  Serial.println("===============================\n");
}

void loop() {
  // Verificação do botão com debounce
  if (digitalRead(BUTTON_PIN) == HIGH) {
    // Simulação de medição diária (na prática seria automática)
    measureDailyRainfall();
    
    // Debounce manual
    delay(500);
    while(digitalRead(BUTTON_PIN) == HIGH) {
      delay(10); // Aguarda soltar o botão
    }
  }
}

// Função para medir a distância com média de várias leituras
float measureDistance() {
  float total = 0;
  int validReadings = 0;
  
  for(int i = 0; i < NUM_READINGS; i++) {
    // Gera pulso de trigger
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);
    
    // Mede o tempo de eco
    unsigned long duration = pulseIn(ECHO_PIN, HIGH, TIMEOUT_US);
    
    // Ignora leituras inválidas
    if(duration > 0 && duration < 25000) {
      float distance = duration * SOUND_SPEED / 2;
      
      // Filtra leituras fora do intervalo esperado
      if(distance > 2.0 && distance < TANK_HEIGHT * 1.1) {
        total += distance;
        validReadings++;
      }
    }
    
    delay(READING_DELAY);
  }
  
  // Retorna média ou -1 para erro
  return (validReadings > 0) ? total / validReadings : -1.0;
}

// Converte distância para volume de chuva (em mm)
float distanceToRainfall(float distance) {
  // Altura da água no recipiente
  float waterHeight = TANK_HEIGHT - distance;
  
  // Área da seção transversal do recipiente (cm²)
  float area = PI * pow(TANK_DIAMETER / 2, 2);
  
  // Volume de água (cm³)
  float volume = waterHeight * area;
  
  // Converte para precipitação em mm (1mm = 1L/m²)
  // Considerando que 1mm de chuva = 1 litro por m²
  float rainfall = (volume / 1000.0) / (area / 10000.0);
  
  return rainfall;
}

void measureDailyRainfall() {
  Serial.println("\nIniciando medição diária...");
  
  float distance = measureDistance();
  
  if(distance < 0) {
    Serial.println("Erro: Não foi possível obter leitura válida");
    return;
  }
  
  // Calcula chuva acumulada
  float dailyRain = distanceToRainfall(distance);
  
  // Atualiza acumulados
  lastRainfall = dailyRain;
  totalRainfall += dailyRain;
  lastMeasureTime = millis();
  
  // Exibe resultados formatados
  Serial.println("===========================================");
  Serial.print("Distancia para a agua: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  Serial.print("Precipitacao diaria: ");
  Serial.print(dailyRain, 1); // 1 casa decimal
  Serial.println(" mm");
  
  Serial.print("Total acumulado: ");
  Serial.print(totalRainfall, 1);
  Serial.println(" mm");
  Serial.println("===========================================\n");
  
  // Simulação de envio para servidor/armazenamento
  Serial.println("Dados registrados. Próxima medição em 24h...");
}