void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  int micValue = analogRead(A0); // read the analog value from pin A0
  Serial.println(micValue); // print the value to the serial monitor
  delay(100);
}
