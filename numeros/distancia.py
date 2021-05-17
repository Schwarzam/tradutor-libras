import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

trig = 18
echo = 24

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
 
def distance():
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
 
    inicio = time.time()
    fim = time.time()
 
    while GPIO.input(echo) == 0:
        inicio = time.time()
    while GPIO.input(echo) == 1:
        fim = time.time()
 
    TempoCorrido = fim - inicio
    distancia = (TempoCorrido * 34300) / 2
 
    return distancia
