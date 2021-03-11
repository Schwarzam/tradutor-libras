import numpy as np
import pandas as pd
import os
from os import listdir
from os.path import isfile, join
from skimage.io import imread

img_rows = 200 ## Comprimento imagem
img_cols = 200 ## Largura 
channels = 3 ## 3 porque eh colorida (3 bandas)_

def ler_imagens(file_paths, img_rows = 200, img_cols = 200, channels = 3):
  images = []
  for file_path in file_paths:
    images.append(imread(file_path))
  images = np.asarray(images, dtype=np.float32)
  images = images / 255.0 #np.max(images) # normalizar
  
  images = images.reshape(images.shape[0], img_rows, img_cols, channels) # reshape para input no keras

  return images
  
label = []
file_paths = []

#Pegar pastas dentro de ./camera
for folder in os.listdir('./camera'):
    if os.path.isdir('./camera/' + folder):
        
        ## Pegar todos arquivos da pasta
        for root, dirs, files in os.walk(os.path.abspath("./camera/" + folder)):
            for file in files:
                file_paths.append(os.path.join(root, file))

        for file in files:
            label.append(str(folder))
            
            
def get_images_array(): ## Funcao que retorna o array com todas imagens das pastas
    array = ler_imagens(file_paths, img_rows, img_cols, channels)
    
    print(len(label), "images loaded")
    return array, label            
