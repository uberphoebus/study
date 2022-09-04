try:
    print('한자리')
    num1 = int(input())
    num2 = int(input())
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print(f'{num1} / {num2} = {num1 / num2}')
except ValueError:
    print('errror ra')