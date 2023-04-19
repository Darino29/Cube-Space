import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ledPin1 =15 
ledPin2 = 18
ledPin3 = 10
btnPin = 22
GPIO.setup(btnPin, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(ledPin1,GPIO.OUT)
GPIO.setup(ledPin2,GPIO.OUT)
GPIO.setup(ledPin3,GPIO.OUT)




while True:
	
		button_state = GPIO.input(btnPin)
		if button_state == False:

			GPIO.output(ledPin1,True)
			time.sleep(2)
			GPIO.output(ledPin1,False)
			GPIO.output(ledPin2,True)
			time.sleep(2)
			GPIO.output(ledPin2,False)
			GPIO.output(ledPin3,True)
			time.sleep(1)
			GPIO.output(ledPin2,True)
			GPIO.output(ledPin1,True)
			time.sleep(1)
			GPIO.output(ledPin1,False)
			GPIO.output(ledPin2,False)
			GPIO.output(ledPin3,False)
				

GPIO.cleanup()
