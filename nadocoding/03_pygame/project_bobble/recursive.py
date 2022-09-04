# 재귀 함수 호출

# for i in range(6):
#     print(i)
#     if i == 5:
#         print('번호 끝')

def count_1(): # 첫 군인
    print(1)
    count_2()
    print('1 끝')

def count_2():
    print(2)
    count_3()
    print('2 끝')

def count_3():
    print(3)
    print('3 끝')

# count_1()

def count(num=1):
    print(num)
    if num == 5:
        print('번호 끝')
    else:
        count(num + 1)
    print(num, '끝')

count()