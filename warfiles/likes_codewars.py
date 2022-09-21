"""
Most Liked Answer:

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
"""

def likes(arg: list):
    c = {
        "a": 'no one likes this',
        "b": lambda arg: '{args} likes this'.format(args=arg[0]),
        "c": lambda arg: '{arg1} and {arg2} like this'.format(arg1=arg[0], arg2 = arg[1]),
        "d": lambda arg: '{arg1}, {arg2} and {arg3} like this'.format(arg1=arg[0], arg2=arg[1], arg3= arg[2]),
        "e": lambda arg:'{arg1}, {arg2} and {arg3} others like this'.format(arg1 = arg[0], arg2=arg[1], arg3=str(len(arg) - 2))
    }

    l = len(arg)
    return c["a"] if l == 0 else c['b'](arg) if l == 1 else c['c'](arg) if l == 2 else c['d'](arg) if l == 3 else c['e'](arg)


if __name__ == "__main__":
    print(likes([]))# 'no one likes this'
    print(likes(['Peter']))# 'Peter likes this'
    print(likes(['Jacob', 'Alex']))# 'Jacob and Alex like this'
    print(likes(['Max', 'John', 'Mark']))#, 'Max, John and Mark like this'
    print(likes(['Alex', 'Jacob', 'Mark', 'Max'])) # 'Alex, Jacob and 2 others like this'