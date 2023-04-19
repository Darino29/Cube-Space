import sys
from twython import Twython
from keys import (
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
        )
import RPi.GPIO as GPIO 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN

while True:
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pushed!")

        
        twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
        )
        message = "Mon premier Tweet avec un Raspberry Pi!"
        twitter.update_status(status=message)print("Tweet réussi : %s " %message)