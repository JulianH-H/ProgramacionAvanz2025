void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(14, OUTPUT);  
  pinMode(15, OUTPUT);
  pinMode(16, OUTPUT);
  pinMode(17, OUTPUT);
  pinMode(18, OUTPUT);
  pinMode(19, OUTPUT);  
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(12, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  digitalWrite(12, LOW);   // turn the LED off by making the voltage LOW
  delay(1000);                      // wait for a second

  digitalWrite(13, HIGH); 
  delay(1000);                      
  digitalWrite(13, LOW);   
  delay(1000);                      

  digitalWrite(14, HIGH); 
  delay(1000);                      
  digitalWrite(14, LOW);   
  delay(1000);

  digitalWrite(15, HIGH); 
  delay(1000);                      
  digitalWrite(15, LOW);   
  delay(1000);

  digitalWrite(16, HIGH); 
  delay(1000);                      
  digitalWrite(16, LOW);   
  delay(1000);

  digitalWrite(17, HIGH); 
  delay(1000);                      
  digitalWrite(17, LOW);   
  delay(1000);

  digitalWrite(18, HIGH); 
  delay(1000);                      
  digitalWrite(18, LOW);   
  delay(1000);

  digitalWrite(19, HIGH); 
  delay(1000);                      
  digitalWrite(19, LOW);   
  delay(1000);

}
