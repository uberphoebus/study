# 1. 그림판 실행 : win + r, mspaint 및 최대화
# 2. 상단의 텍스트 기능을 이용하여 글자 입력
# 3. 5초 대기 후 그림판 종료(저장하지 않음 선택)

import pyautogui
import pyperclip

pyautogui.hotkey('winleft', 'r')
pyautogui.write('mspaint')
pyautogui.press('enter')

pyautogui.sleep(1)

w = pyautogui.getWindowsWithTitle('그림판')[0]
if w.isMaximized == False:
    w.maximize()

pyautogui.hotkey('alt', 'h')
pyautogui.write('t')

pyautogui.click(400, 300, duration=0.25)
pyautogui.sleep(0.5)

pyperclip.copy('영웅문 아바타 트레이딩')
pyautogui.hotkey('ctrl', 'v')

pyautogui.sleep(3)

w.close()
pyautogui.sleep(0.25)
pyautogui.press('n')