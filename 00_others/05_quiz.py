def three():
    print('three', end=' ')
    return 3

def five():
    print('five', end=' ')
    return 5

def seven():
    print('seven', end=' ')
    return 7

# main code
three() > five() > seven()

print(3 > 5 >7) # (3 > 5) and (5 > 7) 이후는 연산하지 않고 끝냄


def a(): print('a'); return True
def b(): print('b'); return False
def c(): print('c'); return True

if a() and b() and c():
    print('good')
else:
    print('bad')