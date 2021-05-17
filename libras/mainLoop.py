##ssh -L 5901:127.0.0.1:5901 -C -N -l desktop 192.168.0.111

from keras.models import load_model
import numpy as np
from extracao_dados import ler_imagens  ## Tem que estar na mesma pasta do arquivo extracao_dados.py
from sklearn import preprocessing
from extracao_dados import get_images_array, get_images_label, tirar_foto
from time import sleep

labels = get_images_label()
le = preprocessing.LabelEncoder()
le.fit(labels)
labels = le.transform(labels)

modelo = load_model('rede_neural.h5')  ## tem que estar na mesma pasta do arquivo

x = True
while x:
	imagem_pronta = tirar_foto()
	respostaprob = modelo.predict(imagem_pronta)
	resposta = np.argmax(respostaprob, axis=-1) ## Vai gerar o numero correspondente a resposta
	print(le.classes_[resposta[0]], 'with', respostaprob.max())

	sleep(0.4)
