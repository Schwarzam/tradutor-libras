import gpiozero
import time

def checar_luminosidade():
    device = gpiozero.DigitalInputDevice(23)
    if device.value == 0:
        return 1
    else:
        return 0
