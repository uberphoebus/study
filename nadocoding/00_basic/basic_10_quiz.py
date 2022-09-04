# 조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
#     출력 : '잘못'
# 조건 2 : 대기 손님이 주문할 수 있는 치킨량은 10마리
#     소진시 사용자 정의 에러 발생하고 종료
#     출력 : '소진'

class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1
while True:
    try:
        print(f'[left chicken] {chicken}')
        order = int(input('how much?'))
        if order > chicken:
            print('un')
        elif order <= 0:
            raise ValueError
        else:
            print(f'[wait no {waiting}] {order} comp')
            waiting += 1
            chicken -= order
        
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print('unval')
    except SoldOutError:
        print('no order')
        break