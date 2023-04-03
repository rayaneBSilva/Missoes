// C++ code
//
void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(LED_BUILTIN, HIGH);
  delay(2000); // Wait for 2000 millisecond(s)
  digitalWrite(LED_BUILTIN, LOW);
  delay(2000); // Wait for 2000 millisecond(s)
   digitalWrite(LED_BUILTIN, HIGH);
  delay(4000); // Wait for 4000 millisecond(s)
  digitalWrite(LED_BUILTIN, LOW);
  delay(4000); // Wait for 4000 millisecond(s)
}