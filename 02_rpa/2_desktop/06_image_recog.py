import pyautogui

# menu = pyautogui.locateOnScreen('kiwoom_menu.png')
# print(menu)

# pyautogui.click(menu)
# pyautogui.moveTo(menu)

# 없을 때
screen = pyautogui.locateOnScreen('screenshot.png')
print(screen)

# 같은 화면이 두개 이상일 때
# for i in pyautogui.locateAllOnScreen('box.png'):
#     print(i)
#     pyautogui.click(i, clicks=2, duration=0.25)

# 속도 개선 1 : GrayScale
# pyautogui.locateOnScreen('kiwoom_menu.png', grayscale=True)

# 속도 개선 2 : 범위 지정
# pyautogui.locateAllOnScreen('kiwoom_menu.png', region=(x, y, width, height))

# 속도 개선 3 : 정확도 조정
# menu = pyautogui.locateOnScreen('kiwoom_menu.png', confidence=0.9)
# pyautogui.moveTo(menu)

# 자동화 대상이 바로 보여지지 않는 경우
# if menu:
#     pyautogui.click(menu)
# else:
#     print('없음')

# while menu is None:
#     menu = pyautogui.locateOnScreen('kiwoom_menu.png', confidence=0.9)
#     print('실패')

# 일정 시간 동안 기다리기(타임아웃)

import time
import sys

# timeout = 10
# start = time.time()
#
# menu = None
# while menu is None:
#     menu = pyautogui.locateOnScreen('kiwoom_menu.png', confidence=0.9)
#     end = time.time()
#     if end - start > timeout:
#         print('시간종료')
#         sys.exit()
# pyautogui.click(menu)


def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
        return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print('target not found')
        sys.exit()

my_click('kiwoom_menu.png', 10)