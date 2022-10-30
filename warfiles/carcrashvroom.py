# The speeding car: "O='`o"
# The other cars: "X"
import itertools
def car_crash(road):
    road = "%r"%''.join(road.split('o')[1])
    print(road)
    for x in itertools.pairwise(road):
        print(x)
        if 'X' in x:
            return True
        elif '\\' in x:
            return False
    return False

cars_around= """
                X
    X   O='`o
                X   """.strip()

car_in_front = """
                    O='`o        X """.strip()

all_directions = """ 
                    X   X  X
        X         O='`o   X
                    X   X   X  """.strip() 

if __name__ == "__main__":
    #print(all_directions.count("X"))


    print(car_crash(cars_around))
    print(car_crash(car_in_front))
    print(car_crash(all_directions))

"""
Awww Gawwwwd:

# The speeding car: "O='`o"
# The other cars: "X"

Best Answer:
def car_crash(road):
    return "O='`oX" in road.replace(' ', '')

I forgot about replace in this instance.  However, I was focused on seeing if it were possible to do what I envisioned
and it was.  
-I learned that it is possible to create a raw string literal from a .join to be able to 'see' the escape characters.

Arguably, I didn't think that simply removing all of the whitespace would make it possible to check for the 'crash' case

May want to see what re module does:

import re
def car_crash(road): return bool(re.search(r'o *X', road))
"""
