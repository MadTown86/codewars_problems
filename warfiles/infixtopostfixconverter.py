"""
https://www.codewars.com/kata/52e864d1ffb6ac25db00017f/train/python
"""



test1 = "2+7*5"
test2 = '3*3/(7+1)'
test3 = '1^2^3'
test4 = '(5-4-1)+9/5/2-7/1/7'
test5 = '3+(5-3*3*7^8)+(4/9*7)+6-6^(4*4*9*0+4)-0' #'3533*78^*-+49/7*+6+644*9*0*4+^-0-'
test6 = '0/9-4^8^(2+4/7)+0^4' # 09/48247/+^^-04^+
teststr = "5+(6-2)*9+3^(7-1)" # 562-9*+371-^+
teststr_revr = ')1-7(^3+9*)2-6(+5'
smallstr = '(1-7-1-9)'


failcase2 = '(5^6-5-(1/8/5)^5)^(8/7/7)^0' #'56^5-18/5/5^-87/7/0^^'


failcase1 = '(9*3/0)  -0/8^2  -3^6/8  +5^((7-7*8)*1/6)*7  +3^9^9' #'93*0/082^/-36^8/-5778*-1*6/^7*+399^^+'

# 93*0/082^/-36^

myans = '93*0/082^/-36^-8/5778*-^+1*6)/7*399^^+'
coran = '93*0/082^/-36^8/-5778*-1*6/^7*+399^^+'

testans = '2-3^6/8'
testans2 = '(7-7*8)'
# Lollerskates, love the guy who developed this >>
# So Rules

"""
Variable or Number then copied directly to output
If operator, it is pushed onto the operator stack.  
If the current operators precedence is lower than that of the operators at the top of the stack or the precedences
equal and the opeartor is left associative, then that operator is popped off the stack and added to the output.

Finally any remaining operators are popped off the stack and added to the output.
"""

"""
Notes on process: left to right precedence exists within the parenthesis and standard 

For instance 7/7/1 isn't 771// it the order has to maintain left to right calculations first or perhaps it is for
readability - 77/1/ is how it would be written, and within parenthesis (5-4-1) isn't 541-- because this would 
potentially confuse order of operations doing 4-1 first, so it is written 54-1- you would have to calculate 5-4 first
"""

"""
List Out Steps:
1. add the 1 but know that it passed a parenthesis (ans = 1)
2. switch 7 and operand (ans = 17-)
3. 
"""
from typing import Any
def to_postfix(t):
    p = {'(': 5, ')': 5, '^': 4, '*': 3, '/': 3, '-': 2, '+': 2}
    left_a = {'(': False, ')': False, '^': False, '*': True, '/': True, '-': True, '+': True}
    ans = ""
    operators = []
    pin_ops = []
    flag = False
    def check(x: str, inp: Any) -> None:
        nonlocal ans
        if len(inp) >= 1:
            if p[x] == p[inp[-1]]:
                if left_a[inp[-1]]:
                    ans += inp.pop()
            elif p[x] < p[inp[-1]]:
                # Write something here to make the comparison for a ^ unique and see if that works.  Or
                # Learn more about the reverse polish notation to see why in this case all of the remaining
                # Operators aren't pushed to the answer.
                while inp:
                        ans += inp.pop()

        inp.append(x)

    for x in t:
        # print(f'ANS: {ans} :: Operators: {operators} :: Pin_Ops: {pin_ops} :: Flag: {flag} : X: {x}')
        if x.isnumeric():
            ans += x
            continue
        else:
            if x == '(':
                flag = True
            elif flag:
                if x == ')':
                    flag = False
                    while pin_ops:
                        ans += pin_ops.pop()

                elif len(pin_ops) >= 1:
                    inside = pin_ops
                    check(x, inside)
                else:
                    if x != ')':
                        pin_ops.append(x)
                    # Write case for when in parentheses but no operators to compare
            elif operators:
                outside = operators
                check(x, outside)
            else:
                # Write case for if no parenthesis and no pre-existing operators
                operators.append(x)
    if operators:
        while operators:
            ans += operators.pop()

    # Write case for dumping remaining stack elements
    return ans



if __name__ == "__main__":
    print(to_postfix(failcase1))
    # print(to_post3(smallstr))

        
        