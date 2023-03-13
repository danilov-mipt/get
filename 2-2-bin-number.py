# в созданном скрипте импортировать модули RPi.GPIO и time
import RPi.GPIO as GPIO
import time

import fileinput

# объявить переменную dac - список указанных на плате номеров GPIO-пинов в области DAC
dac = [10, 9, 11, 5, 6, 13, 19, 26]

# объявить переменную number - список из 0 и 1, длина которого равна длине списка dac
number = [0] * len(dac)

# настроить режим обращения к GPIO
GPIO.setmode(GPIO.BCM)

# одной строкой кода настроить на выход все 8 GPIO-пинов из списка dac
GPIO.setup(dac, GPIO.OUT)

# заполнить список number произвольным набором 0 и 1
number[len(dac) - 1] = 1

# одной строкой кода подать на выход GPIO-пинов из списка dac значения из списка number
GPIO.output(dac, number)

# сделать паузу 10 - 15 секунд, чтобы измерить напряжение
for line in fileinput.input():
	n = int(line)
	for i in range(len(dac)):
		number[i] = (n >> i) % 2
	GPIO.output(dac, number)

# перед завершением скрипта одной строкой кода подать 0 на все использованные GPIO-выходы
GPIO.output(dac, [0] * len(dac))

# перед завершением скрипта вызвать функцию GPIO.cleanup(), чтобы сбросить настройки контроллера GPIO
GPIO.cleanup()
