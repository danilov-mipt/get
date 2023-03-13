import RPi.GPIO as GPIO

GPIO.cleanup()


leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN, pull_up_down=GPIO.PUD_UP)

data = [1] * len(leds)

inv = lambda x: int(not x)

while True:
	for i in range(len(aux)):
		data[i] = int(GPIO.input(aux[i]))
	#data = list(map(inv, data))
	GPIO.output(leds, data)


