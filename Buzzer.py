import RPi .GPIO a s GPIO
import time

buzPin = 12


GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzPin , GPIO.OUT)
GPIO.output(buzPin , GPIO.HIGH)
    while True :
            GPIO.output(buzPin , GPIO.LOW)
            print ("No Beep")
            time.sleep(1)
            GPIO.output(buzPin , GPIO.HIGH)
            print ("Beep")
            time.sleep(1)

GPIO.cleanup()