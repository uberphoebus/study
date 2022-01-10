import pyautogui as pa

size = pa.size() # 현 화면의 스크린 사이즈(가로, 세로)

pa.moveTo(200, 100, duration=0.5)  # 절대위치, 시간 동안
print(pa.position()) # Point(x, y) # 현 위치 출력
pa.moveTo(300, 200, duration=0.5)
print(pa.position()) # Point(x, y)

pa.move(100, 500, duration=0.5) # 상대위치
p = pa.position()
print(p[0], p[1], p.x, p.y)