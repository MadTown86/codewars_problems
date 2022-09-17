"""
*Most Liked Answer:

def chain(value, functions):
    for f in functions:
        value = f(value)
    return value

"""

def chain(init_val, functions):
    localval = init_val
    if functions:
        for func in functions:
            localval = func(localval)

    return localval