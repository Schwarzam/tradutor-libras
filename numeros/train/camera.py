import time
import picamera
import os

with picamera.PiCamera() as camera:
    camera.resolution = (200, 200)
    letra = input('Letra: ')

    try:
        os.mkdir(f'{letra}')
    except:
        pass

    time.sleep(2)
    print(f'starting phtos da letra {letra}')
      
    ninit = int(input('numero inicial: '))
=
    for i in range(200):
        print(f"Foto {i}")
        camera.capture(f'{letra}/imagem{ninit}.jpg')
        ninit = ninit + 1
