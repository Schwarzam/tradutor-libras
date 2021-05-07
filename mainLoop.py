from keras.models import load_model
import numpy as np
from extracao_dados import ler_imagens  ## Tem que estar na mesma pasta do arquivo extracao_dados.py
from sklearn import preprocessing
from extracao_dados import get_images_array, get_images_label, tirar_foto

labels = get_images_label()
le = preprocessing.LabelEncoder()
le.fit(labels)
labels = le.transform(labels)

modelo = load_model('rede_neural.h5')  ## tem que estar na mesma pasta do arquivo

imagem_pronta = tirar_foto()
resposta = modelo.predict(imagem_pronta)
resposta = np.argmax(resposta, axis=-1) ## Vai gerar o numero correspondente a resposta
print(le.classes_[resposta[0]])