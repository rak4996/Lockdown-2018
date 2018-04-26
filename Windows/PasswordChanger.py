#!/usr/bin/env python

import pyautogui
import string
from random import *

currentPassword = ''

def changePassword():
    min_char = 8
    max_char = 16
    all_char = string.ascii_letters + string.punctuation + string.digits

    password = ''.join(choice(all_char) for x in range(randint(min_char, max_char)))
    currentPassword = password

    return currentPassword

def getPassword():
    return currentPassword

def test():
    print(getPassword())
    print(changePassword())
    print(getPassword())

def main():
    pyautogui.hotkey('ctrl', 'alt', 't')
    pyautogui.typewrite('sudo -v')
    pyautogui.typewrite(getPassword())
    pyautogui.typewrite('sudo passwd root')
    changePassword()
    pyautogui.typewrite(getPassword())
    pyautogui.typewrite(getPassword())

    file = open("password.txt", 'w')
    file.write(currentPassword())

#main()
test()


#TODO SCRIPT FOR INSTALLING PIP ON EACH MACHINE
#TODO SCRIPT FOR INSTALLING PYAUTOGUI ON EACH MACHINE