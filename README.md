# Traffic-Light-Raspberry-Pi
# Description
This project detects an object when it is within a certain range and changes the light to green using the HCsr04 ultrasonic sensor on Raspberry Pi. This code also uses an email class with smtplib to send a notication via email when the voltage reading is high. This project assumes that you have already setup your Raspberry Pi and have the Freenove Starter kit directory. If you do not you will need to setup Raspberry Pi and Freenove before you start this project. 

# Materials Needed
## Hardware
1. Raspberry Pi x1
2. GPIO Extension Board & Ribbon Cable x1
3. Breadboard x1
4. HC-SR04 Module
5. Male-to-Female Jumper Wires x10
7. 2 Resistors
8. 1 RGB LED Module


## Software
1. lightTest.py and trafficLight.py from this repository

# Setup and Configuration
## Hardware
Below is the following pinout for this project:
HC-SR04 Ultrasonic Sensor
![image](https://user-images.githubusercontent.com/66813474/167399530-6004d83d-15b5-48e0-a912-4460fa1dacb2.png)

RGB LED
(![image](https://user-images.githubusercontent.com/66813474/167403485-e97b19c0-edbb-4a6e-aa3e-a7be64e33bea.png)

Connect Red LED pin to GPIO 17, Green pin to GPIO 27, Blue LED pin to GPIO 22, and GND to GND. This is important to match the GPIO pins with your code later on. 

_Note: please plug in your cables BEFORE turning on your Raspberry Pi to prevent shorting out your parts._

# Code Setup
Optional code to test RGB LED module:
1. Download and open lightTest.py
2. In lines 7-9, confirm that the values match the GPIO pins connected to the RGB LED Module.
3. Run lightTest.py

1. Download trafficLight.py
2. Open trafficLight.py and  confirm that the values match the GPIO pins connected to the RGB LED Module in lines 52-54.
3. Change the following lines to correspond with the email notication:
    1. line 9: enter the email that you want to send the notification from
    2. line 10: enter the password to the email from line 10
    3. line 99: enter the recipient email
    4. line 100(optional): you can change the email subject
    5. line 101(optional): you can change the contents of the email
4. Run trafficLight.py and place an object in front of the sensor to start.
