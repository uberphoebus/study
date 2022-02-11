# 팩토리얼 재귀함수
# n! = n x (n - 1) x (n - 2) x ... x 1

# 1. n! = n x (n - 1)!
# 2. 1! = 0! = 1

def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

result = factorial(4)
print(result)