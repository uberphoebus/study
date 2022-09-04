class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self) -> str:
        return self.msg

try:
    print('한자리')
    num1 = int(input())
    num2 = int(input())
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError(f'input {num1} {num2}')
    print(f'{num1} / {num2} = {num1 / num2}')
except BigNumberError as err:
    print('errror big num')
    print(err)