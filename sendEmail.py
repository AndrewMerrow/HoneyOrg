import webbrowser
import keyboard
import random
from time import sleep
from emailMessages import *

webbrowser.open('http://gmail.com')
sleep(7)
keyboard.press_and_release('c')
sleep(2)
keyboard.write(recipients[random.randint(0, len(recipients)-1)])
sleep(2)
keyboard.press_and_release('tab')
sleep(1)
keyboard.press_and_release('tab')
sleep(2)
keyboard.write(subjects[random.randint(0, len(subjects)-1)])
sleep(2)
keyboard.press_and_release('tab')
sleep(2)
keyboard.write(messages[random.randint(0, len(messages)-1)])
sleep(2)
#keyboard.press_and_release("ctrl+enter")