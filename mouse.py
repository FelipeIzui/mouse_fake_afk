#pip install pyautogui
#pip install psutil

from cProfile import run
import pyautogui
import psutil
from random import randint
import time
import os
import sys

while(True):
    valor = 0

    for a in range(1920):
        x = randint(0, 1920)
        for b in range(1080):
            y = randint(0, 1080)
            pyautogui.moveTo(x, y, duration = 1)
            valor = valor + 1
            if valor == 5:
                click = randint(1, 3)
                if click == 1:
                    pyautogui.leftClick(x, y)
                if click == 2:
                    pyautogui.middleClick(x, y)
                if click == 3:
                    pyautogui.rightClick(x, y)
                    time.sleep(2)
                    pyautogui.rightClick(x, y)
                print(f'cliquei nas coordenadas: {x}:{y}')
                valor = 0
            time.sleep(1)
    time.sleep(60)


