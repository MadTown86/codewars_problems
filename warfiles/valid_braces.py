"""
https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python
"""

"""
Things I need to do:
1. Parse through the list
2. check for opening brackets of any type and put in stack
3. check for closing brackets and remove from stack
4. If stack empty at the end of iteration = True, else False
"""


"""
***********************
Best Answers
***********************

def validBraces(s, previous = ''):
  while s != previous: previous, s = s, s.replace('[]','').replace('{}','').replace('()','')
  return not s

*Note: Interesting use of single line boolean expression along with a 'function' in a single line

def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''

*Note: Similar concept just used standard format with different boolean expression

import re

class Stack(object):
    def __init__(self): self._vals = []
    def push(self, i): self._vals.append(i)
    def peek(self): return self._vals[-1] if not self.is_empty() else None
    def pop(self): self._vals.pop()
    def is_empty(self): return len(self._vals) == 0

def validBraces(string):
    openers, closers = map(list, ('({[', ')}]'))
    pairs = list(zip(openers, closers))

    s = Stack()
    for char in list(string):
        if char in openers:
            s.push(char)
        elif (char in closers and (s.peek(), char) in pairs):
            s.pop()
    return s.is_empty()

    *Note: With a class no less, and again this 're' module, need to take a look.

"""


def valid_braces(stringer: str) -> bool:
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    pairdict = {'(': ')', '[': ']', '{': '}', ')':'(', ']':'[', '}':'{'}

    openstack = []
    closestack = []

    for char in stringer:
        if char in opening:
            openstack.append(char)
        elif char in closing:
            if pairdict[char] in openstack:
                openstack.pop()
            else:
                return False
    
    if openstack:
        return False
    else:
        return True






if __name__ == "__main__":
    t1 = "(){}[]"
    t2 = "([{}])"
    t3 = "(}"
    t4 = "[(])"
    t5 = "[({})](]"

    testsuite = [t1, t2, t3, t4, t5]
    
    for test in testsuite:
        print(valid_braces(test))
    