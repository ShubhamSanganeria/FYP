#define USE_ARDUINO_INTERRUPTS true
#include <LiquidCrystal_I2C.h>
#include<Wire.h>
#include <PulseSensorPlayground.h>
LiquidCrystal_I2C lcd(0x3f,2,1,0,4,5,6,7,3,POSITIVE);
PulseSensorPlayground pulseSensor;
const int PulseWire=0;
int Threshold=550;
int str=0;

void setup() {
  // put your setup code here, to run once:
  lcd.begin(16,2);
  lcd.clear();
  Serial.begin(9600);
  pinMode(A1,INPUT);
  pulseSensor.analogInput(PulseWire);
  pulseSensor.setThreshold(Threshold);

// Double-check the "pulseSensor" object was created and "began" seeing a signal.
  if (pulseSensor.begin()) {
     Serial.println("We created a pulseSensor Object !"); //This prints one time at Arduino power-up, or on Arduino reset.
     lcd.setCursor(0,0);
     lcd.print(" Heart Rate Monitor");
  }

}

void loop() {
  // put your main code here, to run repeatedly:
int myBPM = pulseSensor.getBeatsPerMinute(); // Calls function on our pulseSensor object that returns BPM as an "int".

float reading=analogRead(A1);
reading= (reading/1024)*5000;
float fhr = reading/10;
fhr=(fhr*9)/5 + 32;
if (pulseSensor.sawStartOfBeat()) {
  if(str!=myBPM){
    // Constantly test to see if "a beat happened".
    str=myBPM;
Serial.println("A HeartBeat Happened ! "); // If test is "true", print a message "a heartbeat happened".
Serial.print("BPM: "); // Print phrase "BPM: "
Serial.println(myBPM); // Print the value inside of myBPM.
Serial.println("Temperature: ");
Serial.println(fhr);
lcd.clear();
lcd.setCursor(0,0);
lcd.print("Temp: ");
lcd.print(fhr);
// If test is "true", print a message "a heartbeat happened".
lcd.setCursor(5,3);
lcd.print("BPM: "); // Print phrase "BPM: "
lcd.print(myBPM);
delay(10000);
}
}
delay(20);
}
