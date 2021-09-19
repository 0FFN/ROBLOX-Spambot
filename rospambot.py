import pyautogui
import pydirectinput
from time import sleep as wait
forever = 1
from os import system
system("title "+"Arc's ROBLOX Spambot")

print(''' 
▄▄▄        ▄▄▄▄· ▄▄▌        ▐▄• ▄     .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·. ▄▄▄▄·       ▄▄▄▄▄
▀▄ █·▪     ▐█ ▀█▪██•  ▪      █▌█▌▪    ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪▐█ ▀█▪▪     •██  
▐▀▀▄  ▄█▀▄ ▐█▀▀█▄██▪   ▄█▀▄  ·██·     ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·▐█▀▀█▄ ▄█▀▄  ▐█.▪
▐█•█▌▐█▌.▐▌██▄▪▐█▐█▌▐▌▐█▌.▐▌▪▐█·█▌    ▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌██▄▪▐█▐█▌.▐▌ ▐█▌·
.▀  ▀ ▀█▄▀▪·▀▀▀▀ .▀▀▀  ▀█▄▀▪•▀▀ ▀▀     ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀·▀▀▀▀  ▀█▄▀▪ ▀▀▀
--> By arc.                                                                        
''')

spam = input("[?] --> Which spam would you like to use?: ")
wait(3)
print("=> Starting spam...")

pyautogui.moveTo(197, 307)
while forever == 1:
    pydirectinput.click()
    pyautogui.typewrite(spam)
    pydirectinput.press('enter')
