import time
import picamera
import os

with picamera.PiCamera() as camera:
    camera.resolution = (200, 200)


    time.sleep(2)
	
    ninit = 1
    for i in range(2):
        print(f"Foto {i}")
        camera.capture(f'{ninit}.jpg')
        ninit = ninit + 1