import pyautogui

# pyautogui.mouseInfo()

# pyautogui.FAILSAFE = False # 계속 실행됨(비추)
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep

for i in range(10):
    pyautogui.move(100, 100)