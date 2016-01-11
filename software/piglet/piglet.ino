// File: piglet.ino
// Version: 1.0
// Description: This code is intended to run on the Teensy 3.2 (or equivalent Arduino).
//              It waits for I2C signals sent from the Raspberry Pi (or any I2C master)
//              and then sends the cooresponding ASCII code via keyboard to the computer.

#include <Wire.h>

void setup()
{
  Wire.begin(8);                // Join I2C bus with address #8
  Wire.onReceive(receiveEvent); // When data is received, run the receiveEvent function
  Serial.begin(9600);           // Set baud rate for serial, not really needed
}

// Wait 100ms between receives
void loop()
{
  delay(100);
}

void receiveEvent(int howMany)
{
  // If there are multiple bytes, then we want to get them all
  while (Wire.available() > 1)
  {
    char a = Wire.read();       // Get key from I2C buffer
    Keyboard.print(a);          // Send key to keyboard
    Serial.print(a);            // Print to serial
    delay(300);                 // Wait 300ms between keypresses
  }
  char b = Wire.read();
  Keyboard.print(b);
  Serial.print(b);
}
