import pyautogui as pa

pa.sleep(1) # 3초 대기
print(pa.position())

# 마우스 클릭
pa.click(1417, 13, duration=0.5)

# 마우스 드래그
# pa.mouseDown()
# pa.mouseUp()

# 더블 클릭
# pa.doubleClick()

# 클릭 횟수
# pa.click(clicks=4)

# 우클릭
# pa.rightClick()

# 휠
# pa.middleClick()

# 드래그
# pa.drag()
# pa.dragTo()

# 스크롤
# pa.scroll(300) # 위로 300