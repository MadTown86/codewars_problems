
""" Answers To String Mix Problem"""
"""
How I struggled:
1. effectively removing the unwanted characters and white space
2. How to store the count with the variable, alphabetically and by quantity
3. The logic behind organizing data by the followign way on output
    -Highest repeat digit count decreasing order
    -String 1 if highest, else 2 or =
"""

def mix(s1, s2):
    hist = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            which = "1" if val1 > val2 else "2" if val2 > val1 else "="
            hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
    return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))

"""
It didn't occur to me that one could just loop through allowed variables.
It also didn't occur to me to simultaneously count the strings so you would have them both available at once.  
I was concerned with having to keep track of 'i' and 'j' and making sure they didn't get out of sync
Then I spent time sorting the lists and making that work with a defaultdict.  So overall just a complete miss

Another really cool way they avoided a bunch of code.  Assign a variable as a nested boolean expression - single line - 
"""

def mix2(s1, s2):
    c1, c2 = [Counter({s: n for s, n in Counter(c).items() if n > 1 and s.islower()}) for c in (s1, s2)]
    return '/'.join(c + ':' + -n * s for n, c, s in
                    sorted((-n, '=12'[(c1[s] == n) - (c2[s] == n)], s) for s, n in (c1 | c2).items()))

"""Answers to land Perimter Question"""

land = lambda a: sum(t == ('X', 'X') for r in a for t in zip(r, r[1:])) * 2

def land_perimeter(a):
    return 'Total land perimeter: ' + str(''.join(a).count('X') * 4 - land(a) - land(zip(*a)))
"""
land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]
"""

def land_perimeter2(arr):
    I, J = len(arr), len(arr[0])

    P = 0
    for i in range(I):
        for j in range(J):
            if arr[i][j] == 'X':
                if i == 0 or arr[i - 1][j] == 'O': P += 1
                if i == I - 1 or arr[i + 1][j] == 'O': P += 1
                if j == 0 or arr[i][j - 1] == 'O': P += 1
                if j == J - 1 or arr[i][j + 1] == 'O': P += 1

    return 'Total land perimeter: ' + str(P)

"""
The Next Bigger Most Liked Solutions
"""

import itertools
def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1

def next_bigger(n):
    nums = list(str(n))
    for i in reversed(range(len(nums[:-1]))):
        for j in reversed(range(i, len(nums))):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                nums[i + 1:] = sorted(nums[i + 1:])
                return int(''.join(nums))
    return -1