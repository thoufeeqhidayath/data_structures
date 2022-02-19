
"""
infinite loop happens if we wont specify base case
fib2(4) -> fib2(3), fib2(2)
fib2(3) -> fib2(2), fib2(1)
fib2(2) -> fib2(1), fib2(0)
fib2(2) -> fib2(1), fib2(0)
fib2(1) -> 1
fib2(1) -> 1
fib2(1) -> 1
fib2(0) -> 0
fib2(0) -> 0
If you count them (and as you will see if you add some print calls), there are 9 calls to
fib2() just to compute the 4th element! It gets worse
"""
from functools import lru_cache


def fibonocii(n:int):
    if n<2:
        return n
    else:
        return fibonocii(n-2) + fibonocii(n-1)

from typing import Dict
memo :Dict[int,int] = {0:0,1:1}
def fib(n:int):
    if n not in memo:
        memo[n] = fib(n-2)+fib(n-1)
    return memo[n]

#with LRU Cache
@lru_cache(maxsize=None)
def fib2(n:int):
    if n<2:
        return n
    else:
        return fib2(n-2) + fib2(n-1)

def fib3(n:int):
    if n ==0 :return 0
    prev = 0
    next = 1
    for i in range(1,n):
        next = next+prev

    print(next)


if __name__ == '__main__':
   print(fibonocii(10))
   print(fib(10))
   print(fib2(4))
   fib3(4)