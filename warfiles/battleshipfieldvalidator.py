"""
https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python
"""

# Reminder: Battleship/4, 2xCruiser/3, 3xDestroyer/2, 4xSubmarine/1 Total: 20
def validate_battlefield(field):
    # Check the field
    t = 0
    arrayflipped = []
    for y in field:
        for x in y:
            t += x
    if t != 20:
        return "Nope, something is wrong!"
    count = 0
    for val in range(len(field[0])-1):
        temp_list = []
        for item in field:
            temp_list.append(item[val])
        arrayflipped.append(temp_list)

    indfield = []
    for l in range(len(field)-1):
        temp_list = []
        for item in range(len(field[l])-1):
            if field[l][item] == 1:
                temp_list.append((l, item))
        indfield.append(temp_list)

    indarrayflipped = []
    for l in range(len(arrayflipped)-1):
        temp_list = []
        for item in range(len(field[l])-1):
            if arrayflipped[l][item] == 1:
                temp_list.append((l, item))
        indarrayflipped.append(temp_list)

    for item in indarrayflipped:
        print(item)

    print("\n")

    for item in indfield:
        print(item)

    print("\n")

    for item in field:
        print(item)

    print("\n")

    for item in arrayflipped:
        print(item)


    return None

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

    print(validate_battlefield(field))



