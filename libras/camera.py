import time
import picamera
import os

with picamera.PiCamera() as camera:
    camera.resolution = (200, 200)
    letra = input('Letra: ')
    # Wait for the automatic gain control to settle
    try:
        os.mkdir(f'{letra}')
    except:
        pass

    time.sleep(2)
    print(f'starting phtos da letra {letra}')
      
    ninit = int(input('numero inicial: '))

#    for filename in camera.capture_continuous(letra + f'/img{ninit}.jpg'):
#        print('Captured %s' % ninit)
#        ninit = ninit + 1
#        time.sleep(1)

    for i in range(100):
        print(f"Foto {i}")
        camera.capture(f'{letra}/imagem{ninit}.jpg')
        ninit = ninit + 1
