//////////////////////////////////////////////////////////////////////////////////////////////////////
// Pin Assignment Constants
//////////////////////////////////////////////////////////////////////////////////////////////////////
// UI
const int potentiometerPin = A5;
const int switchButton = 2;
const int startButton = 3;
const int LED2Pin = 4;
const int LED3Pin = 5;
const int LED4Pin = 6;
// Motors
const int pump1Pin = 9;
const int pump2Pin = 10;
const int mixerPin = 11;
const int stepperDirPin = 12;
const int stepperStepPin = 13;
// Sensors
//const int ultraSoundEcho = 7;
//const int ultraSoundTrig = 8;
const int IRSignal = A2;
const int opticalSignal = A3;
//const int waterLevelSignal = A1;

//////////////////////////////////////////////////////////////////////////////////////////////////////
// Other Constants
//////////////////////////////////////////////////////////////////////////////////////////////////////
const int strengthMultiplicationFactor = 1000;
const int mixerPumpTotalDelay = 10000;
const int IRDetectValue = HIGH;
// const float cupDetectedDistance = 30;

//////////////////////////////////////////////////////////////////////////////////////////////////////
// Reading of input pins
//////////////////////////////////////////////////////////////////////////////////////////////////////
int switchRead;
int startRead;
float potentRead;
float IRRead;

//////////////////////////////////////////////////////////////////////////////////////////////////////
// State Variables
//////////////////////////////////////////////////////////////////////////////////////////////////////
int curr_LEDs = 0;
int LEDLightShowSequence[12] = {0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3};
bool cupDetected = false;
int cupsChecked = 0;

//////////////////////////////////////////////////////////////////////////////////////////////////////
// Setup
//////////////////////////////////////////////////////////////////////////////////////////////////////
void setup() {
  // UI
  pinMode(potentiometerPin, INPUT);
  pinMode(switchButton, INPUT);
  pinMode(startButton, INPUT);
  pinMode(LED2Pin, OUTPUT);
  pinMode(LED3Pin, OUTPUT);
  pinMode(LED4Pin, OUTPUT);
  // Motors
  pinMode(pump1Pin, OUTPUT);
  pinMode(pump2Pin, OUTPUT);
  pinMode(mixerPin, OUTPUT);
  pinMode(stepperDirPin, OUTPUT);
  pinMode(stepperStepPin, OUTPUT);
  // Sensors
  pinMode(IRSignal, INPUT);
  pinMode(opticalSignal, INPUT);
  // Serial for debug printing
  Serial.begin(9600);

  // Sensor we unfortunately have not added yet
  // pinMode(ultraSoundTrig, OUTPUT);
  // pinMode(ultraSoundEcho, INPUT);
}

//////////////////////////////////////////////////////////////////////////////////////////////////////
// LED functions
//////////////////////////////////////////////////////////////////////////////////////////////////////
void updateLEDs() {
  curr_LEDs = ( curr_LEDs + 1 ) % 4;
}

void lightLEDs() {
  digitalWrite(LED2Pin, curr_LEDs > 0);
  digitalWrite(LED3Pin, curr_LEDs > 1);
  digitalWrite(LED4Pin, curr_LEDs > 2);
}

void LEDLightShow() {
  for (byte i = 0; i < 12; i = i + 1) {
    curr_LEDs = LEDLightShowSequence[i];
    lightLEDs();
    delay(50);
  }
}

//////////////////////////////////////////////////////////////////////////////////////////////////////
// Make-Drink functions
//////////////////////////////////////////////////////////////////////////////////////////////////////

void mixDrink() {
  Serial.println("mixDrink");
  digitalWrite(mixerPin, HIGH);
  delay(400); // Run for 400, then begin stopping

  while (digitalRead(IRSignal) != IRDetectValue) {
    Serial.println("looking for default position...");
  }

  delay(97); // delay from detection to make it end in the retracted postion
  digitalWrite(mixerPin, LOW);
}

void makeDrink(int strength) {
  Serial.println("makeDrink");
  // pour the drink
  // start pumping at the same time
  digitalWrite(pump1Pin, HIGH);
  digitalWrite(pump2Pin, HIGH);
  // stop first pump depending on strength
  delay(strength * strengthMultiplicationFactor);
  digitalWrite(pump1Pin, LOW);

  // stop second pump after constant amount of time or fail safe
  delay(mixerPumpTotalDelay - strength * strengthMultiplicationFactor);
  digitalWrite(pump2Pin, LOW);

  // mix the drink
  mixDrink();
}

//////////////////////////////////////////////////////////////////////////////////////////////////////
// Spinning Tray Functions
//////////////////////////////////////////////////////////////////////////////////////////////////////
//Spin plate until optical endstop detects object
void resetPlatePos() {
  Serial.println("resetPlatePos");
  // Clockwise
  digitalWrite(stepperDirPin, HIGH);

  while(digitalRead(opticalSignal) == LOW) {
    Serial.println("Not found");
    digitalWrite(stepperStepPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(stepperStepPin, LOW);
    delay(10);
  }
  Serial.println("Found!");

  for(int i = 0; i < 45; i++) {
    digitalWrite(stepperStepPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(stepperStepPin, LOW);
    delay(10);
  }
  delay(1000);
}

//Spin plate using stepper motor pins by 90 degrees
void spinPlateToNextCup() {
  Serial.println("spinPlateToNextCup");
  // Clockwise
  digitalWrite(stepperDirPin, HIGH);
  
  // If 200 steps is full circle, 50 is 90 degrees
  for(int i = 0; i < 152; i++) { 
    digitalWrite(stepperStepPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(stepperStepPin, LOW);
    delay(10); //Tweak to make slower if needed, so liquid doesn't spill
  }
  
  delay(1000);
}

bool detectCup() {
  // digitalWrite(ultraSoundTrig, LOW);
  // delayMicroseconds(2);
  // digitalWrite(ultraSoundTrig, HIGH);
  // delayMicroseconds(10);
  // digitalWrite(ultraSoundTrig, LOW);

  // duration = pulseIn(ultraSoundEcho, HIGH);
  // distance = (duration*.0343)/2;
  // if (distance < cupDetectedDistance) {
  //   return true
  // }
  // return false
  
  return true;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////
// Start Function
//////////////////////////////////////////////////////////////////////////////////////////////////////
void start(int strength, int count) {
  Serial.println("start");
  Serial.print("Strength out of 10: ");
  Serial.println(strength);
  Serial.print("Number of drinks: ");
  Serial.println(count);

  LEDLightShow();

  cupsChecked = 0;
  resetPlatePos();
  for (int i = 0; i < count; i++) {
    // make sure there is a cup before pouring
    cupDetected = detectCup();
    cupsChecked = cupsChecked + 1;
    while (!cupDetected) {
      // if we already checked the fourth cup, stop checking
      if (cupsChecked == 4) {
        Serial.print("Checked all cups, not enough cups to pour ");
        Serial.print(count);
        Serial.println(" cups.");
        return;
      }
      // If no cup, try spinning again, keeping track of positions checked to check max 4 positions
      spinPlateToNextCup();
      cupDetected = detectCup();
      cupsChecked = cupsChecked + 1;
    }
    makeDrink(strength);
    delay(50); // make sure mixing stick motor has stopped running completely
    spinPlateToNextCup();
  }
  curr_LEDs = 0;
  lightLEDs();
}

//////////////////////////////////////////////////////////////////////////////////////////////////////
// Loop Function
//////////////////////////////////////////////////////////////////////////////////////////////////////
void loop() {
  // UI
  switchRead = digitalRead(switchButton); // 0 or 1
  startRead = digitalRead(startButton); // 0 or 1
  potentRead = analogRead(potentiometerPin) / 100; // 0 to 10
  if (switchRead == HIGH) {
    updateLEDs();
    lightLEDs();
    delay(300);
  }
  if (startRead == HIGH) {
    start(potentRead, curr_LEDs + 1);
  }
}
