from lcd import lcd_init, lcd_string, LCD_LINE_1, LCD_LINE_2
import matplotlib.pyplot as plt
from keras.models import load_model
import numpy as np
from sklearn import preprocessing
from processamento_images import get_images_array, get_metadata, tirar_foto, ler_imagens
from time import sleep
import picamera
from gpiozero import Button

labels, _ = get_metadata('train')

modelo = load_model('../rede_neural_numeros.h5')  ## tem que estar na mesma pasta do arquivo

x = True

with picamera.PiCamera() as camera:
	camera.resolution = (200, 200)
	print('starting camera')
	sleep(2)
	
	but1 = Button(26)
	but2 = Button(21)
	but3 = Button(20)
	but4 = Button(16)
	but5 = Button(19)
	
	string = ''
	lcd_init()
	
	while x:
		camera.capture(f'foto.jpg')
		sleep(0.1)
		imagem_pronta = ler_imagens(['foto.jpg'])

		respostaprob = modelo.predict(imagem_pronta)
		resposta = np.argmax(respostaprob, axis=-1) ## Vai gerar o numero correspondente a resposta
		print(resposta[0], 'with', respostaprob.max())
		
		if resposta[0] == 1 and respostaprob.max() < 0.9:
				resposta[0] = 0
		
		string = string + str(resposta[0])
		lcd_string(string[-16:], LCD_LINE_1)
