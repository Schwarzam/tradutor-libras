import time
import picamera
import os

with picamera.PiCamera() as camera:
    camera.resolution = (200, 200)


    time.sleep(2)
    
    continuar = True
    while continuar:
        letra = input("Insira a letra: ")
        camera.capture(f'{letra}.jpg')
        
        cont = input("Continuar: ")
        if 'n' in cont:
            continuar = False
