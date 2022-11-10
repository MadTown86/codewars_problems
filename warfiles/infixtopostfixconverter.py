"""
https://www.codewars.com/kata/52e864d1ffb6ac25db00017f/train/python
"""

"""

"""

failcase2 = '(5^6-5-(1/8/5)^5)^(8/7/7)^0' #'56^5-18/5/5^-87/7/0^^'
failcase3 = '2*(9/8-1)*6*6*6*8/((9/(8/1^7)*8^3*4)-4-(9*6-5)+(6/1/6+(4-7*0)/5)*9)*5/9/3/3*3/9'
# '298/1-*6*6*6*8*9817^//83^*4*4-96*5--61/6/470*-5/+9*+/5*9/3/3/3*9/'
testans = '2-3^6/8'

"""
Variable or Number then copied directly to output
If operator, it is pushed onto the operator stack.  
If the current operators precedence is lower than that of the operators at the top of the stack or the precedences
equal and the opeartor is left associative, then that operator is popped off the stack and added to the output.

Finally any remaining operators are popped off the stack and added to the output.
"""

"""

"""


from typing import Any
def to_postfix(t):
    p = {'(': 5, ')': 5, '^': 4, '*': 3, '/': 3, '-': 2, '+': 2}
    left_a = {'(': False, ')': False, '^': False, '*': True, '/': True, '-': True, '+': True}
    ans = ""
    operators = []
    pin_ops = []
    flag = False
    countf = 0
    def check(x: str, inp: Any) -> None:
        nonlocal ans
        if len(inp) >= 1:
            # if p[x] == p[inp[-1]]:
            #     if left_a[inp[-1]]:
            #         ans += inp.pop()
            if p[x] <= p[inp[-1]]:
                # Write something here to make the comparison for a ^ unique and see if that works.  Or
                # Learn more about the reverse polish notation to see why in this case all of the remaining
                # Operators aren't pushed to the answer.
                while inp and inp[-1] != '(' and p[x] <= p[inp[-1]] and left_a[x]:
                        ans += inp.pop()
            else:
                while inp and p[x] <= p[inp[-1]]:
                    ans += inp.pop()
        if x != ')':
            inp.append(x)

    for x in t:
        # print(f'ANS: {ans} :: Operators: {operators} :: Pin_Ops: {pin_ops} :: Flag: {flag} : X: {x}')
        if x.isnumeric():
            ans += x
            continue
        else:
            if x == '(':
                countf += 1
                flag = True
                pin_ops.append(x)
            elif flag:
                if x == ')':
                    countf -= 1
                    if countf == 0:
                        flag = False
                    while pin_ops and pin_ops[-1] != '(':
                        ans += pin_ops.pop()
                    if pin_ops:
                        pin_ops.pop()

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
    print(to_postfix(failcase2))
    # print(to_post3(smallstr))

        
"""
This one has some very different solutions that I want to take a look at and review for how their
logic was arranged

#1:
def to_postfix(infix):
  buf = [infix]
  """'Convert infix to postfix'"""
  def accept(chars):
    b = buf[0]
    if len(b) and b[0] in chars:
      buf[0] = b[1:]
      return b[0]
  def atom():
    res = accept('0123456789')
    if res: return res
    accept('(')
    res = expr()
    accept(')')
    return res
  def factor():
    carets = ''
    res = atom()
    while accept('^'):
      res += atom()
      carets += '^'
    return res + carets
  def term():
    res = factor()
    while True:
      c = accept('*/')
      if not c: break
      res += factor() + c
    return res
  def expr():
    res = term()
    while True:
      c = accept('+-')
      if not c: break
      res += term() + c
    return res
  return expr()
  
#2 
#Infix to Postfix Converter: Implements Dijkstra's Shunting-yard algorithm

#simple stack class to be used by the conversion from infix to postfix
class Stack(object):
    def __init__(self):
        self.stack = []

    def getStack(self):
        return ''.join(self.stack)

    def peek(self):
        try:
            return self.stack[0]
        except IndexError as e:
            raise ValueError(e)
        
    def isEmpty(self):
        return len(self.stack)==0
    
    def pop(self):
        try:
            return self.stack.pop(0)
        except IndexError as e:
            raise ValueError(e)

    def push(self, v):
        self.stack.insert(0, v)
#end stack class



#Implements the Shunting-yard algorithm
class Ifix2PfixConverter():
    __EXP_OP = '^'
    __MUL_OP = '*'
    __DIV_OP = '/'
    __ADD_OP = '+'
    __SUB_OP = '-'
    __L_PAREN = '('
    __R_PAREN = ')'

    __precidenceTable = { __EXP_OP : 4,
                          __MUL_OP : 3, __DIV_OP : 3,
                          __ADD_OP : 2, __SUB_OP : 2 }

    __associativityTable  = { __EXP_OP : 'right',
                              __MUL_OP : 'left', __DIV_OP : 'left',
                              __ADD_OP : 'left', __SUB_OP : 'left' }

    def __init__(self, eqn):
        self.infixEqn = eqn
        self.postfixEqn = []
        self.stack = Stack()
        self.convertToPostfix()

    def isLeftAssociative(self, k):
        return 'left' == self.__associativityTable[k]

    def getPostfixEquation(self):
        return ''.join(self.postfixEqn)

    def isOperator(self, k):
        return  (k in self.__precidenceTable)

    def precidence(self,k):
        return self.__precidenceTable[k]

    def isOperand(self, k):
        return k.isalnum()

    def isLeftParen(self,k):
        return k==self.__L_PAREN

    def isRightParen(self,k):
        return k==self.__R_PAREN


    #Implementation of Dijkstra's Shunting-yard algorithm
    def convertToPostfix(self):

        for c in self.infixEqn:
            if self.isOperand(c):
                self.postfixEqn.append(c)
            elif self.isLeftParen(c):
                self.stack.push(c)
            elif self.isRightParen(c):
                while  not self.stack.isEmpty()  and   not self.isLeftParen(self.stack.peek()): 
                    self.postfixEqn.append(self.stack.pop())
                self.stack.pop() #toss the left parenthesis
            elif self.isOperator(c):
                while not self.stack.isEmpty()  and  self.isOperator(self.stack.peek()) \
                      and ( (self.precidence(self.stack.peek()) > self.precidence(c))  or (self.precidence(self.stack.peek()) == self.precidence(c) and self.isLeftAssociative(c))):
                    self.postfixEqn.append(self.stack.pop())
                self.stack.push(c)
            else:
                raise ValueError('Uknown Character [',c,'] Encountered')

        while not self.stack.isEmpty():
            self.postfixEqn.append(self.stack.pop())
#---end class

def to_postfix (infix):
    converter = Ifix2PfixConverter(infix)
    return converter.getPostfixEquation()
#---end function

#3 

LEFT  = lambda a,b: a>=b
RIGHT = lambda a,b: a>b
PREC  = {'+': 2, '-': 2, '*': 3, '/': 3, '^': 4, '(': 1, ')': 1}

OP_ASSOCIATION = {'+': LEFT, '-': LEFT, '*': LEFT, '/': LEFT, '^': RIGHT}


def to_postfix (infix):
    stack, output = [], []
    for c in infix:
        prec = PREC.get(c)
        
        if prec is None: output.append(c)
        elif c == '(':   stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                output.append( stack.pop() )
            stack.pop()
        else:
            while stack and OP_ASSOCIATION[c](PREC[stack[-1]], prec):
                output.append( stack.pop() )
            stack.append(c)
            
    return ''.join(output + stack[::-1])
    
#4

import ast

def to_postfix (infix):
    class PostFixVisitor(ast.NodeVisitor): 
        def visit_BinOp(self, node):
            self.visit(node.left)
            self.visit(node.right)
            self.visit(node.op)

        def visit_Num(self, node):
            postfix.append(str(node.n))
            
        def visit_Add(self, node):
            postfix.append('+')

        def visit_Sub(self, node):
            postfix.append('-')

        def visit_Mult(self, node):
            postfix.append('*')

        def visit_Div(self, node):
            postfix.append('/')

        def visit_Pow(self, node):
            postfix.append('^')

    postfix = []
    p = ast.parse(infix.replace('^', '**'))
    PostFixVisitor().visit(p)
    return ''.join(postfix)
"""