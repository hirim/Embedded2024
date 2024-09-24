import RPi.GPIO as GPIO
import time

from picamera2 import Picamera2, Preview 
from time import sleep

swPin = 14 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

oldSw = 0 
newSw = 0 
cnt = 1 

try : 
	while True : 
		newSw = GPIO.input(swPin) 
		if newSw != oldSw: 
			oldSw = newSw 
			
			if newSw == 1 : 
				print('Click ' + str(cnt)) 
				cnt += 1 

			time.sleep(0.2) 
except KeyboardInterrupt : 
	pass 

GPIO.cleanup() 

