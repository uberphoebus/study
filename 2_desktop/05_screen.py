import pyautogui as pa

# 스크린샷 찍기
img = pa.screenshot()
# img.save('screenshot.png') # 파일로 저장

# pa.mouseInfo()
# 407,1061 247,222,1 #F7DE01

# 픽셀의 RGB
pixel = pa.pixel(407, 1061)
print(pixel)
print(pa.pixelMatchesColor(407, 1061, pixel))
