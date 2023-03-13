import RPi.GPIO as GPIO
import time

bouncetime = 500 # in ms


GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.IN)
GPIO.output(22, 0)


def led_change(self):
	if GPIO.input(23):
		GPIO.output(22, 1)
	else:
		GPIO.output(22, 0)


GPIO.add_event_detect(23, GPIO.BOTH, callback=led_change)

while True:
	time.sleep(1)

GPIO.cleanup()
