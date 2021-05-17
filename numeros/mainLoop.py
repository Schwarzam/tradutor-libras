from lcd import lcd_init, lcd_string, LCD_LINE_1, LCD_LINE_2
lcd_init()
lcd_string('Carregando bibliotecas', LCD_LINE_1)


import matplotlib.pyplot as plt
from keras.models import load_model
import numpy as np
from sklearn import preprocessing
from processamento_images import get_images_array, get_metadata, tirar_foto, ler_imagens
from time import sleep
import picamera
from gpiozero import Button
import sys
from light_sensor import checar_luminosidade
from distancia import distance

operacoes = ['. (fracionar)', '+ (soma)', '- (subtracao)', '* (multiplicacao)', '/ (divisao)']

lcd_string('Carregando modelo', LCD_LINE_1)

labels, _ = get_metadata('train')
modelo = load_model('../rede_neural_tf_numeros.h5')  ## tem que estar na mesma pasta do arquivo

lcd_string('Iniciando camera', LCD_LINE_1)

with picamera.PiCamera() as camera:
    camera.resolution = (200, 200)
    sleep(2)
    
    but1 = Button(26)
    but2 = Button(21)
    but3 = Button(20)
    but4 = Button(16)
    but5 = Button(19)
    
    string = ''
    operation = ''
    
    while not checar_luminosidade():
        lcd_string('Necessita-se iluminação', LCD_LINE_1)
        lcd_string('Aperte but1 p/ continuar. ', LCD_LINE_2)
        but1.wait_for_press()
        
    lcd_string('', LCD_LINE_1)
    lcd_string('', LCD_LINE_2)
    while True:
        if string == '':
            lcd_string('But1 para capturar', LCD_LINE_1)
        
        if but1.is_pressed:
            if distance() > 60:
                lcd_string('Aproximar-se', LCD_LINE_1)
                continue
            elif distance() < 20:
                lcd_string('Afastar-se', LCD_LINE_1)
                continue
            else:
                lcd_string(string[-16:], LCD_LINE_1)
            
            camera.capture(f'foto.jpg')
            imagem_pronta = ler_imagens(['foto.jpg'])
            respostaprob = modelo.predict(imagem_pronta)
            resposta = np.argmax(respostaprob, axis=-1) ## Vai gerar o numero correspondente a resposta
            print(resposta[0], 'with', respostaprob.max())
            string = string + str(resposta[0])
            lcd_string(string[-16:], LCD_LINE_1)
            
            but1.wait_for_release()
        
        if but2.is_pressed:
            string = string[:-1]
            lcd_string(string, LCD_LINE_1)
            
            but2.wait_for_release()
        
        if but3.is_pressed:
            string = ''
            lcd_string(string, LCD_LINE_1)
            lcd_string(string, LCD_LINE_2)
            
            but3.wait_for_release()
            
        if but5.is_pressed:
            exec(f'res = {string}')
            lcd_string("=" + str(res), LCD_LINE_2)
            
        if but4.is_pressed:
            lcd_string('Menu de operacoes.', LCD_LINE_1)
            sleep(1)
            operacao = 0
            
            while True:
                lcd_string(operacoes[operacao], LCD_LINE_1)
                if but5.is_pressed:
                    operacao += 1
                    if operacao > len(operacoes) - 1:
                        operacao = 0
                    lcd_string(operacoes[operacao], LCD_LINE_1)
                    but5.wait_for_release()
                    
                if but4.is_pressed:
                    string = string + operacoes[operacao][0]
                    but4.wait_for_release()
                    
                    lcd_string(string[-16:], LCD_LINE_1)
                    break
            
            
            
            
        
        
        
        

