#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <ArduinoJson.h>
const char *ssid = "AndroidAPB9CF";
const char *password = "rahul12345";

const String endpoint = "http://api.openweathermap.org/data/2.5/weather?q=Patna,in&APPID=";
const String key = "e53f4e88de7c733cd0cb37bb6c117e94";

void setup()
{
  pinMode(16, OUTPUT);
  pinMode(2, OUTPUT);
  digitalWrite(2, HIGH);
  digitalWrite(16, HIGH);
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  Serial.print("\nConnecting to WiFi network");

  while (WiFi.status() != WL_CONNECTED)
  {

    Serial.print(".");
    digitalWrite(2, HIGH);
    delay(500);
    digitalWrite(2, LOW);
    delay(500);
  }

  Serial.println("\nConnected to the WiFi network: " + WiFi.SSID() + " and strength is: " + WiFi.RSSI());
}

void loop()
{
  const int frequency = 1000 * 30; // change 30 to change the number of seconds
  String payload;
  if ((WiFi.status() == WL_CONNECTED))
  { //Check the current connection status
    digitalWrite(2, LOW);
    HTTPClient http;

    http.begin(endpoint + key); //Specify the URL
    int httpCode = http.GET();  //Make the request

    if (httpCode > 0)
    { //Check for the returning code

      payload = http.getString();
      digitalWrite(16, LOW);
      delay(1000);
      digitalWrite(16, HIGH);
      // Serial.println(httpCode);
    }

    else
    {
      Serial.println("Error on HTTP request");
    }
    Serial.flush();
    DynamicJsonDocument doc(1024);
    String json = payload;

    deserializeJson(doc, json);

    JsonObject main = doc["main"];
    float temp = main["temp"]; // 296.15
    temp -= 273.15;
    int pressure = main["pressure"];         // 1019
    int humidity = main["humidity"];         // 78
    int visibility = doc["visibility"];      // 2500
    float wind_speed = doc["wind"]["speed"]; // 3.1
    const char *name = doc["name"];          // "Patna"
    int wind_degree = doc["wind"]["deg"];
    Serial.printf("\nTemperature = %.2f°C\r\n", temp);
    Serial.printf("Humidity = %d %%\r\n", humidity);
    Serial.printf("Pressure = %.3f bar\r\n", pressure);
    Serial.printf("Wind speed = %.1f m/s\r\n", wind_speed);
    Serial.printf("Wind degree = %d°\r\n\r\n", wind_degree);
    http.end(); //Free the resources
    delay(frequency);
  }
  else if (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    digitalWrite(2, HIGH);
    delay(500);
    digitalWrite(2, LOW);
    delay(500);
  }
}