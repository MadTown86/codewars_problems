"""
https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python
"""

"""
Option 1: Parse through linearly, one list to the next, 0-end, count any
Catch 3 out of 10 ships
-Then flip the array, and catch 3 ships
# Doesn't really make sense, might as well just go through it all linearly and create an alg to
identify and continue the direction of the 1's and snake its way along until it doesn't find ones, while checking
the zeroes around.
"""


# Reminder: Battleship/4, 2xCruiser/3, 3xDestroyer/2, 4xSubmarine/1 Total: 20

def fliparray(array):
    array_flipped = []
    for val in range(len(field[0]) - 1):
        temp_list = []
        for item in field:
            temp_list.append(item[val])
        array_flipped.append(temp_list)
    return array_flipped

def returnindexofones(array):
    indfield = []
    for l in range(len(array) - 1):
        temp_list = []
        for item in range(len(array[l]) - 1):
            if array[l][item] == 1:
                temp_list.append((l, item))
        indfield.append(temp_list)
    return indfield

def printall(args):
    for item in args:
        print("\n")
        for line in item:
            print(line)


def validate_battlefield(field):
    # Check the field
    t = 0
    for y in field:
        for x in y:
            t += x
    if t != 20:
        return "Nope, something is wrong!"
    count = 0

    pnts = {}
    indofones = returnindexofones(field)
    for item in indofones:





if __name__ == "__main__":
    field = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                   [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                   [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    testarray = [[0, 0, 0],
                 [0, 1, 0],
                 [0, 0, 0]]

    x, y = 1, 1

    """
    loop through array linearly:
    check and mark 1's:
    check for additional 1's in nsew direction to see if ship continues
    check corners and all the way around ship to make sure free of other ships
    """

    def testaround(array: list, mark: tuple) -> bool:
        x, y = mark
        testequation = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                        (x - 1, y), (x, y), (x + 1, y),
                        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]

        corners = [0, 2, 6, 8]
        nsew = {'N': 1, 'E': 3, 'S': 5, 'W': 7}
        for ind in corners:
            a, b = testequation[ind]
            if array[a][b] == 1:
                return False
        for direction in nsew:

    testaround(testarray, (1, 1))



    mark = (1, 1)
    # check from x-1 to x+1


    testarray2 = [[0, 0, 0],
                  [0, 1, 0],
                  [0, 1, 0]]

    arrayflipped = fliparray(field)
    indfield = returnindexofones(field)
    indarrayflipped = returnindexofones(arrayflipped)
    printall([field, arrayflipped, indfield, indarrayflipped])




