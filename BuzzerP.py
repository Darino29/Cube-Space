import RPi .GPIO a s GPIO
import time

buzPin = 12


GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzPin , GPIO.OUT)
GPIO.output(buzPin , GPIO.LOW)

pwm = GPIO.PWM( buzPin , 50 )
pwm. start(50)
try:
    while True :
        for freq in range ( 100 , 1000 , 50 ):
            pwm.ChangeFrequency(freq)
            time.sleep(0.2)
except KeyboardInterrupt :
    pwm.stop()
    GPIO.cleanup()