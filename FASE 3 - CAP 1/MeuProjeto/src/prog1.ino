#include <Arduino.h>
#include <DHT.h>
#include <ArduinoJson.h>

#define DHTPIN 4       // Pino do sensor DHT22
#define DHTTYPE DHT22
#define LDR_PIN 34     // Pino do sensor de pH (simulado com LDR)
#define PHOS_PIN 12    // Pino do sensor de Fósforo (botão)
#define POTASS_PIN 14  // Pino do sensor de Potássio (botão)
#define RELAY_PIN 26   // Pino do relé (bomba de irrigação)

DHT dht(DHTPIN, DHTTYPE);

void setup() {
    Serial.begin(115200);
    pinMode(PHOS_PIN, INPUT_PULLUP);
    pinMode(POTASS_PIN, INPUT_PULLUP);
    pinMode(LDR_PIN, INPUT);
    pinMode(RELAY_PIN, OUTPUT);
    dht.begin();
}

void loop() {
    int phosphorus = digitalRead(PHOS_PIN);   // Leitura do botão (Fósforo)
    int potassium = digitalRead(POTASS_PIN);  // Leitura do botão (Potássio)
    int ph_value = analogRead(LDR_PIN);       // Leitura do sensor de pH
    float soilHumidity = dht.readHumidity();  // Leitura do sensor de umidade

    // Lógica de acionamento do relé: Se umidade < 40%, ligar bomba
    bool relayStatus = (soilHumidity < 40.0);
    digitalWrite(RELAY_PIN, relayStatus ? HIGH : LOW);

    // Criando JSON
    StaticJsonDocument<200> doc;
    doc["sensor_data"]["phosphorus"] = phosphorus ? "Presente" : "Ausente";
    doc["sensor_data"]["potassium"] = potassium ? "Presente" : "Ausente";
    doc["sensor_data"]["ph_value"] = ph_value;
    doc["sensor_data"]["soil_humidity"] = soilHumidity;
    doc["sensor_data"]["relay_status"] = relayStatus ? "Ativado" : "Desativado";

    // Serializando e imprimindo JSON
    String jsonStr;
    serializeJson(doc, jsonStr);
    Serial.println(jsonStr);

    delay(2000); // Aguarda 2 segundos antes da próxima leitura
}

