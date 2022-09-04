import pyautogui

w = pyautogui.getWindowsWithTitle('메모장')[0]
w.activate()

# 문자열
pyautogui.write('12345')
pyautogui.write('nadocoding', interval=0.25)
# 영문과 숫자만 가능

# 기타 키
pyautogui.write(['t', 'e', 's', 't', 'left', 'left', 'right', 'l', 'a', 'enter'], interval=0.25)
# https://automatetheboringstuff.com/2e/chapter20/
# keyboard attributes

# 특수문자
pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.keyUp('shift')

# 조합키
pyautogui.hotkey('ctrl', 'a')

# 한글 처리
import pyperclip
pyperclip.copy('나도코딩') # 클립보드에 저장
pyautogui.hotkey('ctrl', 'v')

