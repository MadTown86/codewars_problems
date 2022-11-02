def _if(bool, func1, func2):
    if bool:
        return func1()
    elif not bool:
        return func2()

"""
Learned something new: you can just use if bool or if not bool for True False in an if, although I don't know what the benefit is, but I wouldn't
have normally thought to do it that way.
"""