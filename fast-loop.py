import timeit
from numba import njit
import numpy as np

N = 100_000_000

def while_loop(n=N):
    i = 0
    s = 0
    while i < n:
        s += i
        i += 1
    return s

def for_loop(n=N):
    s = 0
    for i in range(n):
        s += i
    return s

def for_loop_inc(n=N):
    s = 0
    for i in range(n):
        s += i
        i += 1
    return s

def for_loop_test(n=N):
    s = 0
    for i in range(n):
        if i < n: pass
        s += i
    return s

def for_loop_inc_test(n=N):
    s = 0
    for i in range(n):
        if i < n: pass
        s += i
        i += 1
    return s

def sum_range(n=N):
    return sum(range(n))

def sum_numpy(n=N):
    return np.sum(np.arange(n))

def sum_math(n=N):
    return (n * (n - 1)) // 2

@njit
def sum_range_jit(n=N):
    return sum(range(n))


def main():
    # print(f'while\t\t : {timeit.timeit(while_loop, number=1)}')
    # print(f'for\t\t : {timeit.timeit(for_loop, number=1)}')
    # print(f'for inc\t\t : {timeit.timeit(for_loop_inc, number=1)}')
    # print(f'for test\t\t : {timeit.timeit(for_loop_test, number=1)}')
    # print(f'for inc test\t : {timeit.timeit(for_loop_inc_test, number=1)}')
    print(f'sum range\t : {timeit.timeit(sum_range, number=1)}')
    print(f'np range\t : {timeit.timeit(sum_numpy, number=1)}')
    # print(f'sum njit\t : {timeit.timeit(sum_range_jit, number=1)}')
    # print(f'sum math\t : {timeit.timeit(sum_math, number=1)}')

if __name__ == '__main__':
    main()