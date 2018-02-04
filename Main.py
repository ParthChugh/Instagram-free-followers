import pyautogui, sys, os
import webbrowser
import time
import names,string,random

    
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
for i in range(1,50):
    os.system("powershell -C Start-Process chrome.exe -ArgumentList @( '-incognito', 'https://www.instagram.com/?hl=en' )")
    pyautogui.hotkey('win','up')
    time.sleep(12)
    pyautogui.moveRel(0, 50)
    pyautogui.click(x=838, y=401)
    name = names.get_first_name()
    pyautogui.typewrite(random_char(5)+'@abc.com')
    pyautogui.click(x=838, y=457)
    pyautogui.typewrite(name)
    pyautogui.moveRel(0, 50)
    pyautogui.click(x=838, y=491)
    pyautogui.typewrite(name+'BOTssssssss')
    pyautogui.click(x=838, y=537)
    pyautogui.typewrite('osheenBOT')
    pyautogui.click(x=838, y=587)
    time.sleep(3)
    os.system("powershell -C Start-Process chrome.exe -ArgumentList @( '-incognito', 'https://www.instagram.com/technical_guruji999/?hl=en' )")
    time.sleep(3)
    pyautogui.click(x=860, y=215)
    time.sleep(3)
    os.system("taskkill /im chrome.exe /f")
