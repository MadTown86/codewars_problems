"""
https://www.codewars.com/kata/52e864d1ffb6ac25db00017f/train/python
"""
teststr = "5+(6-2)*9+3^(7-1)"
teststr_revr = ')1-7(^3+9*)2-6(+5'
smallstr = '(1-7-1-9)'

"""
List Out Steps:
1. add the 1 but know that it passed a parenthesis (ans = 1)
2. switch 7 and operand (ans = 17-)
3. 
"""

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
            lastcharf = False
            ans += x
        if x in andbin:
            lastcharf = True
            if x != '(' and x != ')':
                symb.append(x)
        if y.isnumeric():
            lastcharf = False
            ans += y
        if y in andbin:
            lastcharf = True
            if y != '(' and y != ')':
                symb.append(y)


    for x, y in pairwise(reversed(i)):
        print(counter)
        # if counter == int(len(i))-1:
        #     print("HERE")
        #     print(f'C == Len(): X: {x}, Y:{y}, Counter:{counter}')
        #     parenthesis_check(x, y)
        #     standard_update(x, y)
        # print(f'START OF LOOP:  \nCOUNT: {counter}, \nPARENTF: {parentf}, \nPARENTB: {parentb}, \nX: {x}, Y: {y}')
        if counter == 0:
            print(f'C0 - X: {x}, Y:{y}, Counter:{counter}')
            parenthesis_check(x, y)
            standard_update(x, y)
        
        if counter >= 2 and counter % 2 == 0:
            print(f'C >= 2 : X: {x}, Y:{y}, Counter:{counter}')
            parenthesis_check(x, y)
            standard_update(x, y)

        if counter == len(i)-1:
            print("HERE")
            print(f'C == Len(): X: {x}, Y:{y}, Counter:{counter}')
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

            # print(f'END OF LOOP:  \nCOUNT: {counter}, \nPARENTF: {parentf}, \nPARENTB: {parentb}, \nX: {x}, Y: {y}')
        counter += 1
        # print(symb)
    return ans
                     
                



if __name__ == "__main__":
    print(to_postfix2(teststr))

        
        