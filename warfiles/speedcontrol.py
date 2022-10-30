"""
https://www.codewars.com/kata/56484848ba95170a8000004d
"""
import itertools
import math

def gps(s, x):
    news = (s / 60) / 60
    newx = [abs(a - b) / news for a, b in itertools.pairwise(x)]
    print(newx)
    
    return math.floor(max(newx))


if __name__ == "__main__":
    t1s = (20, [0.0, 0.23, 0.46, 0.69, 0.92, 1.15, 1.38, 1.61])

    print(gps(*t1s))