def likes(arg: list):
    start = 'no one' if len(arg) == 0 else str(arg[0]) if len(arg) == 1 else str(arg[0] + 'and' + arg[1]) if len(arg) == 2 /
                else str(arg[0] + ", " + )
    return f'{}'


if __name__ == "__main__":
    likes([])# 'no one likes this'
    likes(['Peter'])# 'Peter likes this'
    likes(['Jacob', 'Alex'])# 'Jacob and Alex like this'
    likes(['Max', 'John', 'Mark'])#, 'Max, John and Mark like this'
    likes(['Alex', 'Jacob', 'Mark', 'Max']) # 'Alex, Jacob and 2 others like this'