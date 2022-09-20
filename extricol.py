import RPi.GPIO as GPIO
import time

# Definition des variables
vert1 = 36  # Feu vert1
orange1 = 38  # Feu orange1
rouge1 = 40  # Feu rouge1
vert2 = 16  # Feu vert2
orange2 = 18  # Feu orange2
rouge2 = 22  # Feu rouge2
tempo = 3  # Temporisation

GPIO.setmode(GPIO.BOARD)
GPIO.setup(vert1, GPIO.OUT)

GPIO.setup(orange1, GPIO.OUT)
GPIO.setup(rouge1, GPIO.OUT)
GPIO.setup(vert2, GPIO.OUT)
GPIO.setup(orange2, GPIO.OUT)
GPIO.setup(rouge2, GPIO.OUT)


# extinction des leds
GPIO.output(36, 0)
GPIO.output(38, 0)
GPIO.output(40, 0)
GPIO.output(16, 0)
GPIO.output(18, 0)
GPIO.output(22, 0)

# Boucle
try:
    while 1:
        GPIO.output(36, 1)
        GPIO.output(38, 0)
        GPIO.output(40, 0)
        GPIO.output(16, 0)
        GPIO.output(18, 0)
        GPIO.output(22, 1)
        time.sleep(tempo)

        GPIO.output(36, 0)
        GPIO.output(38, 1)
        GPIO.output(40, 0)
        GPIO.output(16, 0)
        GPIO.output(18, 0)
        GPIO.output(22, 1)
        time.sleep(tempo)

        GPIO.output(36, 0)
        GPIO.output(38, 0)
        GPIO.output(40, 1)
        GPIO.output(16, 1)
        GPIO.output(18, 0)
        GPIO.output(22, 0)
        time.sleep(tempo)

        GPIO.output(36, 0)
        GPIO.output(38, 0)
        GPIO.output(40, 1)
        GPIO.output(16, 0)
        GPIO.output(18, 1)
        GPIO.output(22, 0)
        time.sleep(tempo)

except:
    GPIO.cleanup()
