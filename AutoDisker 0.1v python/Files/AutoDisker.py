import pyautogui, time, os

def call_commands():
    time.sleep(5)
    x = open("commands.txt", 'r')
    for word in x:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
    
def call_commands1():
    time.sleep(5)
    x = open("commands1.txt", 'r')
    for word in x:
        pyautogui.typewrite(word)
        pyautogui.press("enter")


def call_commands2():
    time.sleep(5)
    x = open("commands2.txt", 'r')
    for word in x:
        pyautogui.typewrite(word)
        pyautogui.press("enter")

def call_commands3():
    time.sleep(5)
    x = open("commands3.txt", 'r')
    for word in x:
        pyautogui.typewrite(word)
        pyautogui.press("enter")

def call_commands4():
    time.sleep(5)
    x = open("commands4.txt", 'r')
    for word in x:
        pyautogui.typewrite(word)
        pyautogui.press("enter")

def call_commands5():
    time.sleep(5)
    x = open("commands5.txt", 'r')
    for word in x:
        pyautogui.typewrite(word)
        pyautogui.press("enter")


def functions():
    time.sleep(10)
    call_commands()
    time.sleep(1)
    call_commands1()
    time.sleep(1)
    call_commands2()
    time.sleep(1)
    call_commands3()
    time.sleep(1)
    call_commands4()
    time.sleep(1)
    call_commands5()
    time.sleep(1)
    
    print("that's all!")
    
    

functions()


