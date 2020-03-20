#include <Wire.h>
#include <ArduinoJson.h>

void setup()
{
  Wire.begin(8); /* join i2c bus with address 8 */
  Wire.setClock(5000000);
  Wire.onReceive(receiveEvent); /* register receive event */
  Serial.begin(115200);         /* start serial fnor debug */


}

void loop()
{
}

void receiveEvent(int howMany)
{
  String data = "";
  while (Wire.available())
  {
    char c = Wire.read();
    data += c;
  }
  Serial.println(data);
  /*  const size_t capacity = JSON_OBJECT_SIZE(2) + 20;
  DynamicJsonDocument doc(capacity);


  deserializeJson(doc, data);

  int gpio = doc["gpio"]; 
  int state = doc["state"]; 
  Serial.println(gpio);
  Serial.println(state);
  */
}
