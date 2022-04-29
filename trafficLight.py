#Libraries
import RPi.GPIO as GPIO
import time
import smtplib

#Email Notification
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = #email
GMAIL_PASSWORD = #password
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

RUNNING = True

green = 27
red = 17
blue = 22

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

Freq = 100

RED = GPIO.PWM(red, Freq)
GREEN = GPIO.PWM(green, Freq)
BLUE = GPIO.PWM(blue, Freq)

class Emailer:
    def sendmail(self, recipient,  subject, content):
        #Creating the headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " +subject, 
            "To: " + recipient, "MIME-Version 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            RED.start(100)
            GREEN.start(0)
            BLUE.start(0)
            if dist >20.0:
                print ("Measured Distance = %.1f cm" % dist)
                time.sleep(1)
            elif dist < 20.0:
                strdist= str(dist)
                sender = Emailer()
                sendTo = #recipient email
                emailSubject = "IOT Research: Traffic Light "
                emailContent = "This is the Pi in the lab.\n The traffic light has sensed an object. Changing the light to green! Object in range at: "+ strdist
                sender.sendmail(sendTo, emailSubject, emailContent)
                print("Object Detected! changing light to green in 10 seconds")
                time.sleep(10)
                RED.start(0)
                GREEN.start(100)
                BLUE.start(0)
                print("Light green!")
                
                while dist < 20.0:
                    dist = distance()
                    print("light green")
                    if dist < 2.0 or dist > 20.0:
                        print("No object detected, turning light yellow in 10 seconds!")
                        time.sleep(10)
                        print("Turning light yellow")
                        RED.start(100)
                        GREEN.start(100)
                        BLUE.start(0)
                        print("No object detected, turning light red in 10 seconds!")
                        time.sleep(10)
                        print("Turning light red")
                        RED.start(100)
                        GREEN.start(0)
                        BLUE.start(0)
                    time.sleep(2)
            
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

