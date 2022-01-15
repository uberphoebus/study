import pyautogui

fw = pyautogui.getActiveWindow() # 현재 활성화된 창
print(fw.title) # 창의 제목정보
print(fw.size)  # 창의 크기정보
print(fw.left, fw.top, fw.right, fw.bottom)

# pyautogui.click(fw.left + 25, fw.top + 20)

# for w in pyautogui.getAllWindows():
#     print(w)

w = pyautogui.getWindowsWithTitle('영웅문')[0]
print(w)

if w.isActive == False:
    w.activate()

if w.isMinimized == False:
    w.maximize()

w.restore() # 화면 원상복구