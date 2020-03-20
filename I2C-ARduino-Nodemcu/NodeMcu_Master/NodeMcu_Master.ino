#include<Wire.h>


void setup(){
  Wire.begin(D1,D2);
  Wire.setClock(5000000);
  Serial.begin(115200);
 
  }
void loop() {
    Wire.beginTransmission(8); /* begin with device address 8 */
    Wire.write("{\"gpio\":3,\"state\":1}");  /* sends hello string */
    Wire.endTransmission();    /* stop transmitting */
    delay(1000);
}9
