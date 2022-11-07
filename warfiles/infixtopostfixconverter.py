"""
https://www.codewars.com/kata/52e864d1ffb6ac25db00017f/train/python
"""
test1 =
teststr = "5+(6-2)*9+3^(7-1)"
teststr_revr = ')1-7(^3+9*)2-6(+5'
smallstr = '(1-7-1-9)'

"""
List Out Steps:
1. add the 1 but know that it passed a parenthesis (ans = 1)
2. switch 7 and operand (ans = 17-)
3. 
"""
def to_post3(teststr):
    op = string.punctuation
    ans = ""
    operators = []
    inparoperators = []
    prec = {'(': 5, ')': 5, '^': 4, '*': 3, '//': 3, '-': 2, '+': 2}
    parflag = False
    for x in teststr:
        if x.isnumeric():
            ans += x
        else:
            if x == '(':
                parflag = True
                inparoperators.append(x)
            if parflag:
                if x == ')':
                    tl_inparoperators = [(x, prec[y]) for x, y in enumerate(inparoperators)]
                    tl_sort = sorted(tl_inparoperators, key=lambda tupler: tupler[1], reverse=True)
                    while tl_sort:
                        print(tl_sort)
                        for oppar in tl_sort:
                            if oppar[1] == ')' or oppar[1] == '(':
                                inparoperators.pop(inparoperators[oppar[0]])
                            else:
                                ans += inparoperators.pop(oppar[0])
                    parflag = False
                else:
                    inparoperators.append(x)
            else:
                pass



            if teststr.index(x) < len(teststr) and len(operators) >= 2:
                print(operators)
                if prec[x] < prec[operators[len(operators)-1]]:
                    while len(operators) > 0:
                        ans += operators.pop()
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
    print(to_post3(teststr))

        
        