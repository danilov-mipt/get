# в созданном скрипте импортировать модули RPi.GPIO и time
import RPi.GPIO as GPIO
import time

# объявить переменную leds - список указанных на плате номеров GPIO-пинов в области LEDS
leds = [21, 20, 16, 12, 7, 8, 25, 24]

# настроить режим обращения к GPIO
GPIO.setmode(GPIO.BCM)

# одной строкой кода настроить на выход все 8 GPIO-пинов из списка leds
# You can set up more than one channel per call (release 0.5.8 onwards).
GPIO.setup(leds, GPIO.OUT)


GPIO.output(leds, 0)


# написать цикл, поочерёдно включающий 7 - 0 светодиоды на 0.2 с
#for i in range(len(leds)):
#    GPIO.output(leds[i-1], 0)
#    GPIO.output(leds[i], 1)
#    time.sleep(0.2)

# написать цикл, который делает 3 "круга"
for _ in range(3):
    for i in range(len(leds)):
        # Python имеет отрицательные индексы
        # смысл — отсчёт с конца списка
        GPIO.output(leds[i - 1], 0)
        GPIO.output(leds[i], 1)
        time.sleep(0.2)

GPIO.output(leds, 0)
GPIO.cleanup()
