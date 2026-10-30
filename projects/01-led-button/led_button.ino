const int ledPin = 13;
const int buttonPin = 4;
const unsigned long debounceMs = 20;

bool ledState = false;
bool lastReading = HIGH;
bool stableState = HIGH;
unsigned long lastChangeMs = 0;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(115200);
  Serial.println("LED + button ready");
}

void loop() {
  bool reading = digitalRead(buttonPin);

  if (reading != lastReading) {
    lastChangeMs = millis();
    lastReading = reading;
  }

  if ((millis() - lastChangeMs) > debounceMs && reading != stableState) {
    stableState = reading;
    if (stableState == LOW) {
      ledState = !ledState;
      digitalWrite(ledPin, ledState ? HIGH : LOW);
      Serial.println(ledState ? "LED ON" : "LED OFF");
    }
  }
}
