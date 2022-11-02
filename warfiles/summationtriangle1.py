"""
aij = 2j + i + 1 where 0 <= j <= i <=n

side triangle element is n + 1

n + 1 = 2j + i + 1

Definitions:
Permutation Ascent
p = {a_1, a_2, ...} - let this represent a permutation

i represents a permutation ascent so IF a_i < a_i+1

EX: permutation {1, 2, 3, 4} is composed of three ascents - {1, 2}, {2, 3}, and {3, 4}

The number of permutations of length _n having ^k ascents is given by the Eulerian number |n/k|

The total number of ascents in all permutations of order _n is: a_n = 1/2(n-1)n!

Connection between permutation ascents and permutation runs (set of ascending sequences in a permutation)

|n/k| = a(n, k + 1)

polynomial - a mathematical expression involving a sum of powers in one or more variables multiplied by coefficients

a_nx^n + ... a_2x^2 + a_1x + a_0

Hypergeometric Series:
A series for which c_0 = 1 and the ratio of consecutive terms is a rational function of the summation index k.

C_k+1 / C_k = P(k) / C(k) 

P(k) and C(k) are polynomials - C_k is called a hypergeometric term

The functions generated by a hypergeometric series are called hypergeometric functions - if completely factored can be represenented

C_k+1 / C_k = P(k) / C(k) = (k + a_1)(k + a_2)...(k + a_p) / (k + b_1)(k + b_2)...(k + b_1)(k + 1)


2(n+1) + (n + 1) + 1
2*0 + 0 + 1 = 1
2*1 + 1 

Eulers Number Triangle : Definition:

Triangle of numbers A_n,k:
A_n,1 = A_n,n = 1

recurrence relation:
A_n+1,k = kA_n,k + (n + 2 - k)A_n,k-1


"""
# def get_sum(n):
#     if n == 0:
#         return 1
#     else:
#         line = n + 1
#         count = 0
#         sum = 0
#         while line:
#             sum += (line * (line + 1)/2) + (3 * count * line)
#             line -= 1
#             count += 1
#         return sum


# First line will always be n+1 (n * (n + 1)/2)
# rectangle

"""

issue : too slow, times out

options: change looping structure or recursion with functools.cache?
recurse through i, j 

1. while loops with an if expression to alternate between incrementing j and i for each turn
"""

ex_tria = [
    1, 2, 3,
    4, 5,
    7
]


def makethetriangle(n):
    row, col = 0, 0

    equation = lambda row, col: 2 * row + col + 1
    triangle_bin = {}

    #

    def rowcur(n, row, col, colm):
        templ = []
        if colm > col:
            col += 1
            return rowcur(n, row, col, colm)
        if col == n + 1:
            return []
        else:
            templ.append(equation(row, col))
            col += 1
            return templ + rowcur(n, row, col, colm)

    colm = -1
    while row < n + 1:
        row_list = []
        row_list.append(rowcur(n, row, col, colm))
        triangle_bin[str(row)] = row_list[0]
        row += 1
        colm = row

    return triangle_bin


import sys

sys.setrecursionlimit(1000000)
from functools import cache
from functools import partial


def get_sum_buildingtriangle(n):
    if n == 0:
        return 1
    row, col = 0, 0

    equation = lambda row, col: 2 * row + col + 1
    tri_sum = 0



    def rowcur(n, row, col, colm):
        templ = []
        if colm > col:
            col += 1
            return rowcur(n, row, col, colm)
        if col == n + 1:
            return []
        else:
            templ.append(equation(row, col))
            col += 1
            return templ + rowcur(n, row, col, colm)

    colm = -1
    while row < n + 1:
        row_list = []
        row_list.append(rowcur(n, row, col, colm))
        tri_sum += sum(row_list[0])
        row += 1
        colm = row

    return tri_sum


# def get_sum(n):
#     if n == 0:
#         return 1
#     equation = lambda nin: (nin * (nin + 1)/2)
#     count = 1
#     tri_sum = 0
#
#     def deletecur(n):
#         row, col = 0, 0
#
#         equation = lambda row, col: 2 * row + col + 1
#         tri_sum = 0
#         def rowcur(n, row, col, colm):
#             templ = []
#             if colm > col:
#                 col += 1
#                 return rowcur(n, row, col, colm)
#             if col == n + 1:
#                 return []
#             else:
#                 templ.append(equation(row, col))
#                 col += 1
#                 return templ + rowcur(n, row, col, colm)
#
#     def rowcur(nin, count):
#         nonlocal n
#         if nin == 0:
#             res = equation(nin)
#             return res
#         if nin == n:
#             nin -= 1
#             return 0 + rowcur(nin, count)
#         else:
#             res = equation(nin) - count
#             count += 3
#             nin -= 1
#             return res + rowcur(nin, count)
#
#     tri_sum = rowcur(n, count)
#
#     return tri_sum

def get_sum(n):
    if n == 1:
        return 1
    else:
        return 1 + 6*n + (9/2) * n * (n-1) + (2/3) * n * (n - 1) * (n - 2)


if __name__ == "__main__":
    import math
    # print(get_sum(4))
    tbin = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    binzer = [1, 7, 22, 50, 95, 161, 252, 372, 525, 715, 946, 1222, 1547, 1925, 2360, 2856, 3417]
    ans = [1, 7, 22, 50]
    tempbin = []
    for x in tbin:
        tempbin.append(get_sum_buildingtriangle(x))

    newbin1 = list(map(lambda x: math.sqrt(x), [x for x in tempbin]))
    newbin2 = list(map(lambda x, y: math.sqrt(y - x), [x for x in range(len(tempbin))], [y for y in tempbin]))
    newbin3 = list(map(lambda x, y: x - y, tempbin[:-1], tempbin[1:]))
    newbin4 = list(map(lambda x, y: x - y, newbin3[:-1], newbin3[1:]))
    newbin5 = list(map(lambda x, y: x - y, newbin4[:-1], newbin4[1:]))
    print(tempbin)
    print(" " + str(newbin3))
    print("    " + str(newbin4))
    print("     " + str(newbin5))


    """
    I think I finally found the answer to this problem that has reminded me the necessity to review core math concepts...
    
    At least I found on my own that a derived difference between the sums of these polynomial expression goes to 4 so it is solvable
    in the series model
    
    To summarize:
    Create series of differences to see if you can find an arithmetic sequence (meaning increments by a constant)
    
    
    The nth level differences are a sequence
    1st Level differnces is a sequence of a 2nd degree polynomial
    2nd level difference is an arithmetic sequence
    3rd level difference is a constant
    
    https://www.anirdesh.com/math/algebra/sum-of-power-series.php
    
    1 + 6/1!n + 9/2!*n*(n-1) + 4/3!*n(n-1)(n-2)
    
    dingalingaling - ^ .  I can at least solve it mathematically in ONE shot so...for this specific one, I hope the following works.
    """

# from decimal import Decimal as D
# import math
# def get_sum(n):
#     n = D(f'{n}')
#     print(n)
#     return round(D('1') + D('6')*n + (D('9')/(D('2'))) * n * (n-D('1')) + (D('2')/D('3')) * n * (n - D('1')) * (n - D('2')))


"""
def get_sum(n):
    return (n+1)*(n+2)*(4*n+3)//6
"""

