#pip install pyautogui
#pip install psutil

import pyautogui
import psutil
from random import randint
import time
import os
import sys

while True:
    valor = 0

    for a in range(1920):
        x = randint(0, 1920)
        y = randint(120, 1032)
        pyautogui.moveTo(x, y, duration = 1)
        valor = valor + 1
        if valor == 5:
            click = randint(1, 3)
            if click == 1:
                pyautogui.leftClick(x, y)
                print(f'Left click on coords: {x} : {y}')
            if click == 2:
                pyautogui.middleClick(x, y)
                print(f'Right click on coords: {x} : {y}')
            if click == 3:
                pyautogui.rightClick(x, y)
                time.sleep(2)
                pyautogui.rightClick(x, y)
                print(f'Middle click on coords: {x} : {y}')
            valor = 0
        time.sleep(5)
time.sleep(60)


