import pyautogui as pa

# pa.mouseInfo()

# pa.FAILSAFE = False # 계속 실행됨(비추)
pa.PAUSE = 1 # 모든 동작에 1초씩 sleep

for i in range(10):
    pa.move(100, 100)