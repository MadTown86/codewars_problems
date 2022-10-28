"""
Seems like recursion here is

Example from test case: I put it here because it shows a different method, one that I was trying to envision.
Good use of imagery for rabbit and turtle as well. (turtle and hare)

def loop_size(node):
    turtle, rabbit = node.next, node.next.next

    # Find a point in the loop.  Any point will do!
    # Since the rabbit moves faster than the turtle
    # and the kata guarantees a loop, the rabbit will
    # eventually catch up with the turtle.
    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next.next

    # The turtle and rabbit are now on the same node,
    # but we know that node is in a loop.  So now we
    # keep the turtle motionless and move the rabbit
    # until it finds the turtle again, counting the
    # nodes the rabbit visits in the mean time.
    count = 1
    rabbit = rabbit.next
    while turtle != rabbit:
        count += 1
        rabbit = rabbit.next

    # voila
    return count

This worked but I had to set the upper bounds of recursion

Something is messed up with this: It fails via exit code 139 more than half the time, but when it does get a correct run
it is faster at 7384ms
def loop_sizein(node: Any, tupler: list):
    if id(node) in tupler:
        return len(tupler[tupler.index(id(node)):])
    else:
        tupler.append(id(node))
        return loop_sizein(node.next(), tupler)

def loop_size(node: Any):
    return loop_sizein(node, [])


This passed too but seemed slower: 11183ms
from typing import Any
def loop_size(node: Any) -> int:
    n = node
    idl = []
    while n:
        if id(n) in idl:
            return len(idl[idl.index(id(n)):])
        else:
            idl.append(id(n))
        n = n.next
    return 0

"""
from _collections_abc import Iterable
from typing import Any

class Node():
    def __init__(self):
        self.pointer = None

    def __next__(self):
        if self.pointer:
            return self.pointer
        else:
            raise StopIteration

def loop_size(node: Any):
    n = node
    idl = []
    while n:
        if id(n) in idl:
            return len(idl[idl.index(id(n)):])
        else:
            idl.append(id(n))
        n = n.next
    return 0



N1 = Node()
N2 = Node()
N3 = Node()
N4 = Node()
N1.pointer = N2
N2.pointer = N3
N3.pointer = N4
N4.pointer = N2

print(loop_size(N1))




