"""
https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python
"""

from itertools import pairwise

# Reminder: Battleship/4, 2xCruiser/3, 3xDestroyer/2, 4xSubmarine/1 Total: 20
subbin = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

# Flip array to get other ships
def fliparray(array):
    array_flipped = []
    for val in range(len(field[0]) - 1):
        temp_list = []
        for item in field:
            temp_list.append(item[val])
        array_flipped.append(temp_list)
    print("\n")
    for line in array_flipped:
        print(line)
    print("\n")
    return array_flipped

# Parse array to return list of (x, y) index pairs for 1's in index
def returnindexofones(array):
    indfield = []
    for l in range(len(array)):
        for item in range(len(array[l])):
            if array[l][item] == 1:
                indfield.append((l, item))

    return indfield

# Check length of ships by indexes from 'returnindexofones'
def returnsubtractions(arr):
    ret = []
    count = [0]
    ccc = 1
    toview = []
    for x, y in pairwise(arr):
        a, b = x
        c, d = y
        summ = (d-a) + (c-b)
        if summ == 1:
            ccc += 1
            count.append(ccc)
        else:
            ccc = 1
            count.append(0)

        toview.append(((x, y), (a, b, c, d), (summ)))

    print(toview)

    print(count)

    for ind in range(len(count)-1):
        if ind < len(count):
            if count[ind] != 0:
                print(count[ind-1], count[ind], count[ind+1])
                if count[ind-1] < count[ind] and count[ind+1] < count[ind]:
                    print(f'{count[ind]}')
                    ret.append(count[ind])
                    print(f'RET: {ret}')
                else:
                    continue
        if ind == len(count):
            if count[ind] != 0:
                if count[ind-1] < count[ind]:
                    ret.append(count[ind])

    return ret

# Returns count of subs
def count_sub(field):

    indofones = returnindexofones(field) # List of pnts where 1's are located in matrix
    countsub = []
    for x, y in indofones:
        neighbors = 0
        surroundsound = [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y),
                         (x - 1, y - 1), (x + 1, y - 1), (x - 1, y - 1), (x + 1, y - 1)]

        for a, b in surroundsound:
            print(a, b)
            if a < 0 or b < 0:
                continue
            elif field[a][b] == 1:
                neighbors += 1

        if neighbors == 0:
            countsub.append(1)

    return countsub

def neighbors(field):
    indofones = returnindexofones(field)  # List of pnts where 1's are located in matrix
    neighbors = 0
    for x, y in indofones:
        surroundsound = [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y),
                         (x - 1, y - 1), (x + 1, y - 1), (x - 1, y - 1), (x + 1, y - 1)]

        for a, b in surroundsound:
            if a < 0 or b < 0:
                continue
            elif field[a][b] == 1:
                neighbors += 1
    print(f'NEIGHBORS: {neighbors}')
    return neighbors


# Sinks the ships
def sinkships(loads):
    for payload in loads:
        for bomb in payload:
            try:
                subbin.remove(bomb)
            except: # Ship Too Large Exception
                return "Nope, something is wrong!"

def validate_battlefield(arr):
    # Check the field for total 1 count
    t = 0
    for a in field:
        for b in a:
            t += b
    if t != 20:
        return "Nope, something is wrong!"

    farray = fliparray(arr)
    pnts_flipped = returnindexofones(farray)
    pnts = returnindexofones(arr)

    payloads = [returnsubtractions(pnts), returnsubtractions(pnts_flipped), count_sub(field)]

    sinkships(payloads)

    if subbin:
        return 'Yep!, Seems alright'
    else:
        return 'Nope, something is wrong!'







if __name__ == "__main__":
    field =       [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                   [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                   [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                   [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                   [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    print(neighbors(field))

    validate_battlefield(field)





