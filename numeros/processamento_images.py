import numpy as np
import pandas as pd
import os
from os import listdir
from os.path import isfile, join
from skimage.io import imread
from picamera import PiCamera
from time import sleep
from PIL import Image, ImageOps
from io import BytesIO  
import cv2
            
img_rows = 200 ## Comprimento imagem
img_cols = 200 ## Largura 
channels = 3 ## 3 porque eh colorida (3 bandas)_

def ler_imagens(file_paths, img_rows = 200, img_cols = 200, channels = 3):
  images = []
  for file_path in file_paths:
    im = imread(file_path)
    im = cv2.applyColorMap(im, cv2.COLORMAP_JET)
    images.append(im)

  images = np.asarray(images, dtype=np.float32)
  images = images / 255.0 #np.max(images) # normalizar
  images = images.reshape(images.shape[0], img_rows, img_cols, channels) # reshape para input no keras
  return images
  
def get_metadata(dataSet):
  label = []
  file_paths = []

  #Pegar pastas dentro de ./camera
  for folder in os.listdir(f'./{dataSet}'):
      if os.path.isdir(f'./{dataSet}/' + folder):
          ## Pegar todos arquivos da pasta
          for root, dirs, files in os.walk(os.path.abspath(f"./{dataSet}/" + folder)):
              for file in files:
                  file_paths.append(os.path.join(root, file))
                  label.append(str(folder))
  
  return label, file_paths
            
def get_images_array(): ## Funcao que retorna o array com todas imagens das pastas
    array = ler_imagens(file_paths, img_rows, img_cols, channels)
    
    print(len(label), "images loaded")
    return array, label            

def get_images_label(): ## Funcao que retorna o array com todas imagens das pastas
    return label  


