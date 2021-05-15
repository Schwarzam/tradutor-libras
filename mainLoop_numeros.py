##ssh -L 5901:127.0.0.1:5901 -C -N -l desktop 192.168.0.111
import matplotlib.pyplot as plt
from keras.models import load_model
import numpy as np
from sklearn import preprocessing
from extracao_dados_numeros import get_images_array, get_metadata, tirar_foto, ler_imagens
from time import sleep
import picamera


labels, _ = get_metadata('train')

modelo = load_model('rede_neural_numeros.h5')  ## tem que estar na mesma pasta do arquivo

x = True

with picamera.PiCamera() as camera:
	camera.resolution = (200, 200)
	print('starting camera')
	sleep(2)
	while x:
		camera.capture(f'foto.jpg')
		sleep(0.1)
		imagem_pronta = ler_imagens(['foto.jpg'])
		plt.imsave('foto1.jpg', imagem_pronta[0])

		respostaprob = modelo.predict(imagem_pronta)
		resposta = np.argmax(respostaprob, axis=-1) ## Vai gerar o numero correspondente a resposta
		print(resposta[0], 'with', respostaprob.max())

		sleep(0.8)
