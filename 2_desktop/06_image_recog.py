import pyautogui as pa

menu = pa.locateOnScreen('kiwoom_menu.png')
print(menu)

# pa.click(menu)
pa.moveTo(menu)

# 없을 때
screen = pa.locateOnScreen('screenshot.png')
print(screen)

# 같은 화면이 두개 이상일 때
for i in pa.locateAllOnScreen('box.png'):
    print(i)
    pa.click(i, clicks=2, duration=0.25)

# 속도 개선 1 : GrayScale
