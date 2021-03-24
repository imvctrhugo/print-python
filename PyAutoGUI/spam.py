#pip install pyautogui
#Instalacao da biblioteca necessaria para o funcionamento do programa.

#Importacao das bibliotecas necessarias.
import pyautogui
from time import sleep

sleep(1) #Breve sleep de 1 segundo para dar tempo de ir ate o local onde o script sera spammado (WhatsApp, Instagram...)

script = open("breakingbad-pilot.txt", 'r') #Variavel "script" irá abrir o arquivo "breakingbad-pilot.txt" em modo de leitura ('r'), onde ira armazenar toda o texto.

for texto in script: #Essa estrutura de repeticao percorre cada texto dentro do "script", escreve o que encontrar e aperta "enter". Tudo isso possivel atraves da biblioteca PyAutoGUi.
    pyautogui.typewrite(texto)
    pyautogui.press("enter")

#BY VICTOR, 24 DE MARCO DE 2021.
#https://youtu.be/64hnN1e_uFM