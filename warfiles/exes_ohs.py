"""
Count exes and oh's

Liked Example:

def xo(s):
    return s.lower().count('x') == s.lower().count('o')
"""

def xo(s):
    countx = s.count('x') + s.count('X')
    counto = s.count('o') + s.count('O')

    if countx == counto:
        return True
    else:
        return False