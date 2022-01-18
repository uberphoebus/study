import time
import keyboard
from PIL import ImageGrab

def screenshot():
    # _20220118_102030
    curr_time = time.strftime('_%Y%m%d_%H%M%S')
    img = ImageGrab.grab()
    img.save(f'image{curr_time}.png')

keyboard.add_hotkey('F9', screenshot) # F9키로 저장
# keyboard.add_hotkey('ctrl+shift+s', screenshot)
keyboard.wait('esc') # 사용자가 esc를 누를 때까지 수행