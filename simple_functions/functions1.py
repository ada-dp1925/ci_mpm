from functools import cache

__all__ = ['my_sum','factorial','calc_sin']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot

@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

def calc_sin(x,n):
    sin=x
    for i in range(n):
        sin+=((-1)**(i+1))*(x**(2*(i+1)+1))/factorial(2*(i+1)+1)
    return sin
