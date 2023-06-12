import time, pyautogui
from time import sleep


usr_spm = str(input('>>> enter the text : '))
spam = usr_spm + '\n'


quantity = int(input('>>> amount of spam texts sent : '))

f = open('texts.txt', 'w')

f.write(spam*quantity)

sleep(3)

f = (open("texts.txt", 'r'))
for words in f:
    pyautogui.typewrite(words)
    pyautogui.press('enter')

f.close
