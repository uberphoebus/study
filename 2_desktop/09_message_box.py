import pyautogui

pyautogui.countdown(3)
print('시작')

# pyautogui.alert('실패', '경고') # 확인 버튼만 있는 팝업
result = pyautogui.confirm('계속 진행?', '확인')
print(result)

result = pyautogui.prompt('입력하셈', '입력')
print(result)

result = pyautogui.password('암호입력')
print(result)