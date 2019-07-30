int buttonPin = 2;
int buttonState=0;
void setup() {
  Serial.begin(9600); // use the same baud-rate as the python side
  pinMode(buttonPin, INPUT);
 
}
void loop() {
   buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {
    Serial.println("send"); // write a string
    
  } 
  else if(buttonState == LOW){
    Serial.println("not pushed");
    }
}
  
  

  
 
  
 
