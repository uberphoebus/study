import pyautogui

pyautogui.sleep(1) # 3초 대기
print(pyautogui.position())

# 마우스 클릭
pyautogui.click(1417, 13, duration=0.5)

# 마우스 드래그
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# 더블 클릭
# pyautogui.doubleClick()

# 클릭 횟수
# pyautogui.click(clicks=4)

# 우클릭
# pyautogui.rightClick()

# 휠
# pyautogui.middleClick()

# 드래그
# pyautogui.drag()
# pyautogui.dragTo()

# 스크롤
# pyautogui.scroll(300) # 위로 300