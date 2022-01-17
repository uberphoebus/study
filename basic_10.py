try:
    print('나누기')
    nums = []
    n1 = int(input())
    n2 = int(input())
    nums = [n1, n2] #, n1/n2]
    print(f'{nums[0]} / {nums[1]} = {nums[2]}')
except ValueError:
    print('에러 발생')
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print(err)