
/*
//---------------------------------------------------------------------------------//|
CSC465 Senior Design                                                              //|
    South Dokota State University                                                 //|
          -------Audio Visualization Sound Data Collection Software-------------- //|
                        Author: Ben Morse bmorse@wi.rr.com 262-470-6519           //|
                        Co-Authors: Ethan Rasmussen                               //|
                                    Bailey Wessels                                //|
//---------------------------------------------------------------------------------//|
 * 
 * Description:
 * This program is designed to work with 4 sound sensors connected to an Arduino microcontroller. The goal of this
 * program is to record the time of arrival of sound detected by each sensor, utilizing external interrupts and
 * direct port manipulation for optimized performance. The recorded times are sent over the serial connection
 * when all four sensors have received a sound input.
 *
 * This program can be used for applications such as sound localization, acoustic source identification, or
 * time difference of arrival estimation in various systems like robotics, security, or environmental monitoring. * 
 * Pin Connections:
 *--------------------------------//|
 *      Sensor 1: ->Pin 2       //|
 *      Sensor 2: ->Pin 3       //|
 *      Sensor 3: ->Pin 4       //|
 *      Sensor 4: ->Pin 5       //|
 *--------------------------------//|
 * Data Format:
 * The transmitted data over the serial connection is in CSV format. Each row represents a set of readings from the
 * sensors, and the columns are the sensor IDs and their respective time of arrival values in microseconds.
 * Example: "1,2,3,4\n123456,234567,345678,456789\n"
 * 
 * Note:
 * While the program is optimized to minimize the chances of missing inputs, it may still miss high-frequency
 * inputs or struggle with performance in certain scenarios. In such cases, consider using a more powerful
 * microcontroller or a microprocessor.
 */

#include <Arduino.h>
#include <string.h>
//------------------------------------------------------------//|
#define SENSOR1_ID 1                                         //|
#define SENSOR2_ID 2                                         //|
#define SENSOR3_ID 3                                         //|
#define SENSOR4_ID 4                                         //|
                                                             //|
const byte sensor1Pin = 2;                                   //|
const byte sensor2Pin = 3;                                   //|
const byte sensor3Pin = 4;                                   //|
const byte sensor4Pin = 5;                                   //|
                                                             //|
const byte sensor1BitMask = digitalPinToBitMask(sensor1Pin); //|
const byte sensor2BitMask = digitalPinToBitMask(sensor2Pin); //|
const byte sensor3BitMask = digitalPinToBitMask(sensor3Pin); //|
const byte sensor4BitMask = digitalPinToBitMask(sensor4Pin); //|
                                                             //|
volatile uint32_t sensor1Value = 0;                          //|
volatile uint32_t sensor2Value = 0;                          //|
volatile uint32_t sensor3Value = 0;                          //|
volatile uint32_t sensor4Value = 0;                          //|
                                                             //|
volatile bool sensor1Active = true;                          //|
volatile bool sensor2Active = true;                          //|
volatile bool sensor3Active = true;                          //|
volatile bool sensor4Active = true;                          //|
int triggerSequence[4];                                      //|
uint32_t triggerSequenceTimes[4];                            //|
int firstTime;                                               //|
//------------------------------------------------------------//|

String dataFormat = "";
int numTriggered = 0; // Keep track of number of triggered sensors

//-----------------------//|
void resetTimers();      //|
void sensor1Interrupt(); //|
void sensor2Interrupt(); //|
void sensor3Interrupt(); //|
void sensor4Interrupt(); //|
void compare_uint32_t(); //|
//-----------------------//|
int compare_uint32_t(const void *a, const void *b) 
{
  uint32_t ua = *(const uint32_t*)a;
  uint32_t ub = *(const uint32_t*)b;
  return ua < ub ? -1 : ua > ub ? 1 : 0;
}


/*vvvvvv*    Main Code      *vvvvvvvvvvvvv*/
void setup() 
{
  Serial.begin(115200);
  dataFormat = String(SENSOR1_ID) + "," + String(SENSOR2_ID) + "," + String(SENSOR3_ID) + "," + String(SENSOR4_ID) + "\n";

  pinMode(sensor1Pin, INPUT_PULLUP);
  pinMode(sensor2Pin, INPUT_PULLUP);
  pinMode(sensor3Pin, INPUT_PULLUP);
  pinMode(sensor4Pin, INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt(sensor1Pin), sensor1Interrupt, RISING);
  attachInterrupt(digitalPinToInterrupt(sensor2Pin), sensor2Interrupt, RISING);
  attachInterrupt(digitalPinToInterrupt(sensor3Pin), sensor3Interrupt, RISING);
  attachInterrupt(digitalPinToInterrupt(sensor4Pin), sensor4Interrupt, RISING);
}

void loop() 
{
  
  while (numTriggered < 4) {
    if (!sensor1Active && !sensor2Active && !sensor3Active && !sensor4Active) {
      numTriggered = 0;
      String dataString = String(sensor1Value) + "," + String(sensor2Value) + "," + String(sensor3Value) + "," + String(sensor4Value) + "\n";
      Serial.print(dataFormat);
      Serial.print(dataString);
      delay(100); // Wait for a brief period before resetting the timers
      resetTimers();
    }
    else {
      noInterrupts(); // Disable interrupts temporarily
      
      if (!sensor1Active) numTriggered++;
      if (!sensor2Active) numTriggered++;
      if (!sensor3Active) numTriggered++;
      if (!sensor4Active) numTriggered++;
      
      interrupts(); // Re-enable interrupts
    }
  }
}




void sensor1Interrupt()
{
  if (sensor1Active) {
    sensor1Value = micros();
    triggerSequence[numTriggered] = 1;
    sensor1Active = false;
    *portInputRegister(digitalPinToPort(sensor1Pin)) &= ~sensor1BitMask;
  }
}

void sensor2Interrupt()
{
  if (sensor2Active) {
    sensor2Value = micros();
    triggerSequence[numTriggered] = 2;
    sensor2Active = false;
    *portInputRegister(digitalPinToPort(sensor2Pin)) &= ~sensor2BitMask;
  }
}

void sensor3Interrupt()
{
  if (sensor3Active) {
    sensor3Value = micros();
    triggerSequence[numTriggered] = 3;
    sensor3Active = false;
    *portInputRegister(digitalPinToPort(sensor3Pin)) &= ~sensor3BitMask;
  }
}

void sensor4Interrupt()
{
  if (sensor4Active) {
    sensor4Value = micros();
    triggerSequence[numTriggered] = 4;
    sensor4Active = false;
    *portInputRegister(digitalPinToPort(sensor4Pin)) &= ~sensor4BitMask;
  }
}

void resetTimers()
{
  uint32_t values[] = {sensor1Value, sensor2Value, sensor3Value, sensor4Value}; 
  char message_data[256] = ""; // Make sure the buffer is large enough to hold the data

  for (int i = 0; i < 4; i++) 
  {
      char temp[64]; // Temporary buffer to hold the formatted string
      sprintf(temp, "%d\n", sensor1Value);
      strcat(message_data, temp);
  }

  *portInputRegister(digitalPinToPort(sensor1Pin)) |= sensor1BitMask;
  *portInputRegister(digitalPinToPort(sensor2Pin)) |= sensor2BitMask;
  *portInputRegister(digitalPinToPort(sensor3Pin)) |= sensor3BitMask;
  *portInputRegister(digitalPinToPort(sensor4Pin)) |= sensor4BitMask;
  sensor1Value = 0;
  sensor2Value = 0;
  sensor3Value = 0;
  sensor4Value = 0;
  sensor1Active = true;
  sensor2Active = true;
  sensor3Active = true;
  sensor4Active = true;


  // Print the delay times with the sensor IDs
  Serial.println("newsound\n");
  
}




 