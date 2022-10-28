"""
5
Initial function takes the N value
 for x in range (1, N+1):
    partition = x + N-x
    if partition not in answerbin:
        answerbin.append(partition)
> return func(n-x)
"""


def func(num):
    count = 0
    if num < 3:
        return num
    for x in range(1, num):
        count += func(num-x)
    return count

print(func(5))




    





        



