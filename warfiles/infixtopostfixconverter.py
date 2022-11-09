"""
https://www.codewars.com/kata/52e864d1ffb6ac25db00017f/train/python
"""
test1 = "2+7*5"
test2 = '3*3/(7+1)'
test3 = '1^2^3'
test4 = '(5-4-1)+9/5/2-7/1/7'
test5 = '3+(5-3*3*7^8)+(4/9*7)+6-6^(4*4*9*0+4)-0' #'3533*78^*-+49/7*+6+644*9*0*4+^-0-'
test6 = '0/9-4^8^(2+4/7)+0^4' # 09/48247/+^^-04^+
teststr = "5+(6-2)*9+3^(7-1)"
teststr_revr = ')1-7(^3+9*)2-6(+5'
smallstr = '(1-7-1-9)'

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
def to_post4(t):
    p = {'(': 5, ')': 5, '^': 4, '*': 3, '/': 3, '-': 2, '+': 2}
    left_a = {'(': False, ')': False, '^': True, '*': False, '/': True, '-': False, '+': False}
    ans = ""
    operators = []
    pin_ops = []
    flag = False
    def check(x: str, inp: Any) -> None:
        nonlocal ans
        if len(inp) >= 1:
            if p[x] > p[inp[len(inp)-1]]:
                inp.append(x)
            elif p[x] == p[inp[len(inp) - 1]]:
                if left_a[inp[len(inp) - 1]]:
                    ans += inp.pop()
                    inp.append(x)
                else:
                    inp.append(len(inp) - 1)
            elif p[x] < p[inp[0]]:
                ans += inp.pop()
                inp.append(x)

    for x in t:
        print(f'ANS: {ans} :: Operators: {operators} :: Pin_Ops: {pin_ops} :: Flag: {flag} : X: {x}')
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



def to_post3(teststr):
    op = string.punctuation
    ans = ""
    operators = []
    inpar_operators = []
    prec = {'(': 5, ')': 5, '^': 4, '*': 3, '//': 3, '-': 2, '+': 2}
    parflag = False
    for x in teststr:
        if x.isnumeric():
            ans += x
        else:
            # Parenthesis case - enter branch
            if x == '(':
                parflag = True
                inpar_operators.append(x)
            # While iterating within parenthesis
            if parflag:
                if x == ')':
                    tl_inparoperators = [(x, prec[y]) for x, y in enumerate(inpar_operators)]
                    tl_sort = sorted(tl_inparoperators, key=lambda tupler: tupler[1], reverse=True)
                    while len(inpar_operators) > 0:
                        for operator in tl_sort:
                            print(tl_sort)
                            if operator[1] == '(' or ')':
                                inpar_operators.pop(inpar_operators.index(operator[1]))
                            else:
                                ans += inpar_operators.pop(inpar_operators.index(operator[1]))
                    # Reset parflag and exit branch
                    parflag = False
                else:
                    # Keeps adding operators until
                    inpar_operators.append(x)
            # Operator case, external
            if operators:
                if prec[x] <= prec[operators[len(operators)-1]]:
                    for opex in reversed(operators):
                        if prec[x] <= prec[operators[len(operators)-1]]:
                            ans += operators.pop()
                else:
                    operators.append(x)
            else:
                operators.append(x)

    return ans, operators

# With Lists
def to_postfix(orig):
    # Parenthesis first then recreate org string
    copyl = orig[:]
    mod_1 = copyl.replace('(', '  ')
    mod_1 = mod_1.replace(')', '  ')
    mod1_list = mod_1.split('  ')

    for lot in mod1_list:
        if lot[0].isnumeric() and lot[len(lot)-1].isnumeric():
            temp_ands = []
            temp_ters = []
            for x in reversed(lot):
                if x.isnumeric():
                    temp_ands.append(x)
                else:
                    temp_ters.append(x)
    return res
from itertools import pairwise
import string

exampleloop = \
[(')', '1'),
('-', '7'),
('(', '^'),
('3', '+'),
('9', '*'),
(')', '2'),
('-', '6'),
('(', '+'),
('+', '5')]

def to_postfix2(i):
    andbin = string.punctuation
    ans = ""
    symb = []
    counter = 0
    parentf = False
    parentb = False
    parentf_flag = 0
    lastcharf = False

    def parenthesis_check(x, y):
        nonlocal parentf, parentf_flag, parentb, counter
        if x == ")" or y == ")" and parentf == False:
            parentf = True
            parentf_flag = counter
        if x == "(" or y == "(" and parentb == False:
            if parentf_flag < counter:
                parentb = True

    def standard_update(x, y):
        nonlocal ans, symb, andbin, lastcharf, lastcharf
        if x.isnumeric():
            ans += x
        if x in andbin:
            if x != '(' and x != ')':
                symb.append(x)
        if y.isnumeric():
            ans += y
        if y in andbin:
            if y != '(' and y != ')':
                symb.append(y)

    for x, y in pairwise(reversed(' ' + i)):
        if counter == len(i):
            print("HERE")
            print(f'C == Len(): X: {x}, Y:{y}, Counter:{counter}')
            parenthesis_check(x, y)
            standard_update(x, y)
        
        if counter == 0:
            print(f'C0 - X: {x}, Y:{y}, Counter:{counter}')
            parenthesis_check(x, y)
            standard_update(x, y)
        
        if counter >= 2 and counter % 2 == 0:
            print(f'C >= 2 : X: {x}, Y:{y}, Counter:{counter}')
            parenthesis_check(x, y)
            standard_update(x, y)

        if parentf and parentb:
            print(f'X: {x}, Y:{y}, Counter:{counter}')
            ans += str(symb.pop(0))
            print(f'ANSWER AT PARENTEND: {ans}')
            parentf = False
            parentb = False

        if lastcharf == True:
            if symb:
                ans += symb.pop(0)
                lastcharf == False

        print(f'ANS: {ans}')

            # print(f'END OF LOOP:  \nCOUNT: {counter}, \nPARENTF: {parentf}, \nPARENTB: {parentb}, \nX: {x}, Y: {y}')
        counter += 1
        # print(symb)
    return ans
                     
                



if __name__ == "__main__":
    print(to_post4(teststr))
    # print(to_post3(smallstr))

        
        