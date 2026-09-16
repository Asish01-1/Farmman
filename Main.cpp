// #include <DHT.h>

// #define DHTPIN D2
// #define DHTTYPE DHT11

// DHT dht(DHTPIN, DHTTYPE);

// void setup() {
//   Serial.begin(115200);
//   delay(2000);

//   Serial.println("ROBOAI DHT TEST");

//   dht.begin();
// }

// void loop() {
//   float temperature = dht.readTemperature();
//   float humidity = dht.readHumidity();

//   if (isnan(temperature) || isnan(humidity)) {
//     Serial.println("DHT ERROR");
//   } else {
//     Serial.print("Temperature: ");
//     Serial.print(temperature);
//     Serial.println(" C");

//     Serial.print("Humidity: ");
//     Serial.print(humidity);
//     Serial.println(" %");
//   }

//   delay(3000);
// }

// #include <DHT.h>

// #define DHTPIN D2
// #define DHTTYPE DHT11

// DHT dht(DHTPIN, DHTTYPE);

// void setup() {
//   Serial.begin(115200);
//   delay(2000);

//   Serial.println("================================");
//   Serial.println("ROBOAI DHT11 TEST");
//   Serial.println("================================");

//   dht.begin();
// }

// void loop() {

//   float temperature = dht.readTemperature();
//   float humidity = dht.readHumidity();

//   if (isnan(temperature) || isnan(humidity)) {

//     Serial.println("DHT ERROR");

//   } else {

//     Serial.print("Temperature: ");
//     Serial.print(temperature);
//     Serial.println(" °C");

//     Serial.print("Humidity: ");
//     Serial.print(humidity);
//     Serial.println(" %");
//   }

//   Serial.println("----------------------------");

//   delay(3000);
// }

// #define SOIL_PIN A0

// void setup() {
//   Serial.begin(115200);
//   delay(1000);

//   Serial.println("================================");
//   Serial.println("ROBOAI SOIL MOISTURE TEST");
//   Serial.println("================================");
// }

// void loop() {

//   int soilValue = analogRead(SOIL_PIN);

//   Serial.print("Soil Moisture Raw Value: ");
//   Serial.println(soilValue);

//   delay(1000);
// }

// #include <ESP8266WiFi.h>
// #include <ESP8266HTTPClient.h>
// #include <DHT.h>

// #define DHTPIN D2
// #define DHTTYPE DHT11
// #define SOIL_PIN A0

// const char* ssid = "iQOO";
// const char* password = "Asish$326";

// const char* serverURL =
//   "https://farmman-onp7.onrender.com/sensor-data";

// DHT dht(DHTPIN, DHTTYPE);

// void setup() {
//   Serial.begin(115200);

//   dht.begin();

//   WiFi.begin(ssid, password);

//   Serial.print("Connecting to WiFi");

//   while (WiFi.status() != WL_CONNECTED) {
//     delay(500);
//     Serial.print(".");
//   }

//   Serial.println();
//   Serial.println("WiFi Connected!");
//   Serial.print("IP: ");
//   Serial.println(WiFi.localIP());
// }

// void loop() {

//   float temperature = dht.readTemperature();
//   float humidity = dht.readHumidity();

//   int soilRaw = analogRead(SOIL_PIN);

//   if (isnan(temperature) || isnan(humidity)) {
//     Serial.println("DHT ERROR");
//     delay(3000);
//     return;
//   }

//   // Temporary raw soil value
//   int soilMoisture = soilRaw;

//   Serial.println("-----------------------------");
//   Serial.print("Temperature: ");
//   Serial.print(temperature);
//   Serial.println(" C");

//   Serial.print("Humidity: ");
//   Serial.print(humidity);
//   Serial.println(" %");

//   Serial.print("Soil Raw: ");
//   Serial.println(soilMoisture);

//   if (WiFi.status() == WL_CONNECTED) {

//     WiFiClientSecure client;
//     client.setInsecure();

//     HTTPClient http;

//     http.begin(client, serverURL);
//     http.addHeader("Content-Type", "application/json");

//     String json = "{";
//     json += "\"tempreature\":" + String(temperature, 1) + ",";
//     json += "\"humidity\":" + String(humidity, 1) + ",";
//     json += "\"soil_moisture\":" + String(soilMoisture);
//     json += "}";

//     Serial.println("Sending:");
//     Serial.println(json);

//     int httpCode = http.POST(json);

//     Serial.print("HTTP Response: ");
//     Serial.println(httpCode);

//     if (httpCode > 0) {
//       String response = http.getString();

//       Serial.println("Server Response:");
//       Serial.println(response);
//     }

//     http.end();
//   }

//   delay(10000);
// }

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <DHT.h>

#define DHTPIN D2
#define DHTTYPE DHT11
#define SOIL_PIN A0
#define BUZZER D5


const char* ssid = "iQOO";
const char* password = "Asish$326";

const char* serverURL =
  "https://farmman-onp7.onrender.com/sensor-data";

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);

  pinMode(BUZZER, OUTPUT);
  digitalWrite(BUZZER, LOW);

  dht.begin();

  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi Connected!");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
}

void loop() {

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  int soilMoisture = analogRead(SOIL_PIN);

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("DHT ERROR");
    delay(3000);
    return;
  }

  Serial.println("-----------------------------");

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" C");

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");

  Serial.print("Soil Raw: ");
  Serial.println(soilMoisture);

  if (WiFi.status() == WL_CONNECTED) {

    WiFiClientSecure client;
    client.setInsecure();

    HTTPClient http;

    http.begin(client, serverURL);
    http.addHeader("Content-Type", "application/json");

    String json = "{";
    json += "\"tempreature\":" + String(temperature, 1) + ",";
    json += "\"humidity\":" + String(humidity, 1) + ",";
    json += "\"soil_moisture\":" + String(soilMoisture);
    json += "}";

    Serial.println("Sending:");
    Serial.println(json);

    int httpCode = http.POST(json);

    Serial.print("HTTP Response: ");
    Serial.println(httpCode);

    if (httpCode > 0) {

      String response = http.getString();

      Serial.println("Server Response:");
      Serial.println(response);

      // Check hardware command
      if (response.indexOf("\"hardware_command\":1") >= 0) {

        Serial.println("COMMAND 1 → BUZZER ON");

        digitalWrite(BUZZER, HIGH);

      } else {

        Serial.println("NO WATER COMMAND → BUZZER OFF");

        digitalWrite(BUZZER, LOW);
      }
    }

    http.end();
  }

  delay(10000);
}