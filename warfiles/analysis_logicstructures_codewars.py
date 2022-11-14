
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




"""

land = lambda a: sum(t == ('X', 'X') for r in a for t in zip(r, r[1:])) * 2

def land_perimeter(a):
    return 'Total land perimeter: ' + str(''.join(a).count('X') * 4 - land(a) - land(zip(*a)))
    
"""

"""
land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]
"""
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

# Next Bigger

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

"""

# Battleship Problem
"""
def validateBattlefield(field):
    n, m = len(field), len(field[0])
    def cell(i, j):
        if i < 0 or j < 0 or i >= n or j >= m: return 0
        return field[i][j]
    def find(i, j):
        if cell(i + 1, j - 1) or cell(i + 1, j + 1): return 10086
        if cell(i, j + 1) and cell(i + 1, j): return 10086
        field[i][j] = 2
        if cell(i, j + 1): return find(i, j + 1) + 1
        if cell(i + 1, j): return find(i + 1, j) + 1
        return 1
    num = [0] * 5
    for i in xrange(n):
        for j in xrange(m):
            if cell(i, j) == 1:
                r = find(i, j)
                if r > 4: return False
                num[r] += 1
    [tmp, submarines, destroyers, cruisers, battleship] = num
    return battleship == 1 and cruisers == 2 and destroyers == 3 and submarines == 4
"""

"""
from scipy.ndimage.measurements import label, find_objects, np
def validate_battlefield(field):
    field = np.array(field)
    return sorted(
        ship.size if min(ship.shape) == 1 else 0
        for ship in (field[pos] for pos in find_objects(label(field, np.ones((3,3)))[0]))
    ) == [1,1,1,1,2,2,2,3,3,4]
"""

# Nesting Structure Comparison

"""
def same_structure_as(original,other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            if not same_structure_as(o1, o2): return False
        else: return True
    else: return not isinstance(original, list) and not isinstance(other, list)
"""

"""
def same_structure_as(original, other):
    if type(original) == list == type(other):
        return len(original) == len(other) and all(map(same_structure_as, original, other))
    else:
        return type(original) != list != type(other)
"""

"""
def same_structure_as(a, b):
    return (False if not (isinstance(a, list) and isinstance(b, list)) or len(a) != len(b)
            else all(same_structure_as(c, d) for c, d in zip(a, b) if isinstance(c, list)))
"""

"""
s = same_structure_as = lambda a, b: type(a) == type(b) == list and len(a) == len(b) and all(map(s, a, b)) if type(a) == list else 1
"""

# Infix to Postfix

"""
def to_postfix(infix):
    output = ""
    stack = []
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    for c in infix:
        if c.isalnum():
            output += c
        elif c == '(':
             stack.append(c)
        elif c == ')':
            while stack[-1] != "(":
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != "(" and \
                (precedence[stack[-1]] > precedence[c] or
                    (precedence[stack[-1]] == precedence[c] and c != "^")):
                output += stack.pop()
            stack.append(c)
    while stack:
        output += stack.pop()
    return output
"""

"""
def to_postfix (infix):
    for i in range(10):
        infix = infix.replace(str(i), f"x({i})")
    infix = infix.replace('^', '**')
    class x:
        def __init__(self, v): self.v = str(v)
        def __add__(self, y): return x(self.v + y.v + '+')
        def __sub__(self, y): return x(self.v + y.v + '-')
        def __mul__(self, y): return x(self.v + y.v + '*')
        def __truediv__(self, y): return x(self.v + y.v + '/')
        def __pow__(self, y): return x(self.v + y.v + '^')
    return eval(infix).v
"""

# Most frequently used words in a text

"""
from collections import Counter
import re


def top_3_words(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w,_ in c.most_common(3)]
"""

"""
import re
from collections import Counter

top_3_words=lambda t:[w for w,c in Counter(re.findall("'*[a-z][a-z']*",t.lower())).most_common(3)]
"""

"""
import re

def top_3_words(text):
    re_non_valid = re.compile('[^a-z\' ]')
    re_chars = re.compile('[a-z]')
    text = text.lower()
    text = ' '.join([x for x in re_non_valid.sub(' ',text).split() if re_chars.search(x)])
    words = {}
    top = {}                    # Dictionary with no more than 3 words
    for word in text.split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
        top[word] = words[word] # Add the new word to the top
        if len(top) > 3:        # If the top is too big remove the worst word
            top.pop(min(top, key=top.get))
    return sorted(top, key=top.get, reverse=True)
"""