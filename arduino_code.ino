void setup() {
  // Initialize serial communication at 9600 baud:
  Serial.begin(9600);

  // Set pin modes for the digital pins:
  pinMode(10, INPUT);
  pinMode(11, INPUT);
}

void loop() {
  // Check if either digital pin 10 or 11 is HIGH
  if (digitalRead(10) == HIGH || digitalRead(11) == HIGH) {
    // Send a '!' character if the condition is true
    Serial.println('!');
  } else {
    // Read and send the analog value from pin A0
    Serial.println(analogRead(A0));
  }

  // Small delay to avoid saturating the serial communication
  delay(10); // Increased to 10ms for smoother plotting
}
