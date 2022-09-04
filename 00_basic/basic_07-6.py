gun = 10

def check(sold):
    global gun # 전역공간의 변수를 사용
    gun = gun - sold
    print(f'함수 내 : {gun}')

def check2(gun, sold):
    gun = gun - sold
    print(f'함수 내 : {gun}')
    return gun


print(f'전체 총 : {gun}')
gun = check2(gun, 2)
print(f'남은 총 : {gun}')