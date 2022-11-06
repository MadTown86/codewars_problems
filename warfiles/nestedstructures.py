"""
https://www.codewars.com/kata/520446778469526ec0000001/train/python
"""

"""
Muumi Answer: 

def same_structure_as(original,other):
    left_is_list = isinstance(original, list)
    right_is_list = isinstance(other, list)
    if not left_is_list:
        return not right_is_list
    return (
        left_is_list == right_is_list and
        len(original) == len(other) and
        all(same_structure_as(a, b) for a, b in zip(original, other)))

Other Answers - Most Liked:
#1
def same_structure_as(original,other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            if not same_structure_as(o1, o2): return False
        else: return True
    else: return not isinstance(original, list) and not isinstance(other, list)

#2
def same_structure_as(original, other):
    if type(original) == list == type(other):
        return len(original) == len(other) and all(map(same_structure_as, original, other))
    else:
        return type(original) != list != type(other)            
"""

testcase = [1, [1, 1], 1], [1, [1, 1], 1]
failcase = [1, '[', ']'], ['[', ']', 1]
failcase2 = [], {}

from typing import Iterable
from typing import Any
# Answer courtesy of Muumi
def same_structure_as(arg1: list, arg2: list) -> bool:
    if isinstance(arg1, int) and isinstance(arg2, int):
        return True
    if isinstance(arg1, str) or isinstance(arg2, str):
        return True
    elif isinstance(arg1, Iterable) and isinstance(arg2, Iterable):
        if isinstance(arg1, str) and isinstance(arg2, str):
            return True
        if type(arg1) != type(arg2):
            return False
        if len(arg1) != len(arg2):
            return False
        for x, y in zip(arg1, arg2):
            if not same_structure_as(x, y):
                return False
    else:
        return False
    return True


if __name__ == "__main__":
    print(same_structure_as(*failcase))




# from typing import Any
# from typing import Iterable

# # Didn't read problem right, but I like this for checking to see if they are exactly the same so don't want to change it
# # Also somewhat successful recursion

# testcase = [1, [1, 1]], [[1, 1], 1]

# def same_structure_as(sandwich, wienerschnitzel):
    
#     def chew(food: list[list, Any], calories, bites) -> list:
#         bites += 1
#         if not food:
#             return (calories, bites)
#         else:
#             for bite in food:
#                 if isinstance(bite, Iterable):
#                     chew(bite, calories, bites)
#                     continue
#                 else:
#                     calories.append(bite)
#                     continue
#         return (calories, bites)
    
#     cal = []
#     count = 0
#     res = chew(sandwich, cal, count)

#     cal = []
#     count = 0
#     res2 = chew(wienerschnitzel, cal, count)

#     if res == res2:
#         return True
#     else:
#         return False


# Practice with strings as an extension of last night
"""
def same_structure_as(arg1: list, arg2: list) -> str:
    # Could count them, but doesn't prove order
    ret = [(str(arg1).count('['), str(arg1).count(']')), (str(arg2).count('['), str(arg2).count('['))]

    s1 = str(arg1)
    s2 = str(arg2)

    s1r = s1[:]
    for char in s1:
        if char == '[' or char == ']':
            continue
        else:
            s1r = s1r.replace(char, '')

    s2r = s2[:]
    for char in s2:
        if char == '[' or char == ']':
            continue
        else:
            s2r = s2r.replace(char, '')

    if s2r == s1r:
        return True
    else:
        return False
"""

# if __name__ == "__main__":
#     print(same_structure_as([1, [1, 1]], [1, [1, 1]]))
                    