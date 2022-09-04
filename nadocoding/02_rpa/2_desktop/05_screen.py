import pyautogui

# 스크린샷 찍기
img = pyautogui.screenshot()
# img.save('screenshot.png') # 파일로 저장

# pyautogui.mouseInfo()
# 407,1061 247,222,1 #F7DE01

# 픽셀의 RGB
pixel = pyautogui.pixel(407, 1061)
print(pixel)
print(pyautogui.pixelMatchesColor(407, 1061, pixel))
