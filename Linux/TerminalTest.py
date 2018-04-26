import pyautogui

def main():
    pyautogui.hotkey('command', 'space')
    pyautogui.typewrite('terminal')
    pyautogui.press('enter')
    pyautogui.typewrite('sudo -v')
    pyautogui.typewrite()

main()

