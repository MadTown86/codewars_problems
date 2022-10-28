"""
5
Initial function takes the N value
 for x in range (1, N+1):
    partition = x + N-x
    if partition not in answerbin:
        answerbin.append(partition)
> return func(n-x)

Alternate Answers:
1#
from sys import setrecursionlimit
setrecursionlimit(1000)

def odd_even_compositions(n, cache = {0: 1}):
    if n in cache: return cache[n]
    count = 0
    for i in range(1, n + 1):
        if i != 1 and i != n and i % 2 != n % 2: continue
        count += odd_even_compositions(n - i, cache)
    cache[n] = count
    return odd_even_compositions(n, cache)

2#
def odd_even_compositions(n):
    if n < 2:
        return 1
    if n % 2:
        return odd_even_compositions(n - 2) * 3
    else:
        return odd_even_compositions(n - 1) * 2
"""

from functools import cache

@cache
def func(num):
    count = 0
    if num == 0:
        return 1
    if num < 3:
        return num
    for x in range(1, num + 1):
        if num % 2 == 0:
            if x % 2 == 0 or x == 1:
                count += func(num - x)
            else:
                continue
        else:
            if x == 1 or x % 2 == 1:
                count += func(num - x)
            else:
                continue
    return count


print(func(0))
print(func(3))
print(func(4))
print(func(7))
print(func(28))
