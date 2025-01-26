
void setup() {
  // initialize the serial communication:
  Serial.begin(9600)
  pinMode(10, INPUT)
  pinMode(11, INPUT)
  

}

void loop() {
  
  if((digitalRead(10) == 1 || (digitalRead(11) == 1)){
    Serial.println('!');
  }
  else{
    //send the value of analog input 0:
    Serial.println(analogRead(AQ));

  }
  //Wait a little bit so the serial data does not saturate
  delay(1)

}
