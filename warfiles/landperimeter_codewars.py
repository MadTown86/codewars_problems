"""
land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]), "Total land perimeter: 60")
land_perimeter(["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]), "Total land perimeter: 52")
land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"]), "Total land perimeter: 40")
land_perimeter(["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"]), "Total land perimeter: 54")
land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"]), "Total land perimeter: 40")
"""

#simplified test

"""
XXXXXOOO
OOXOOOOO
OOOOOOXO
XXXOOOXO
OXOXXOOX

4, 3, 7, 6, 5, 9, 8, 7, 6, 10, 9
+4, -1, +4, -2, +4, -3, +4, -2, +4, -1 
"""

"""
From Muumi
arr[i][j] is arr[i-1][j]
"""
def land_perimeter(args: list[str]):
    perimeter = 0
    for i in range(len(args)):
        for j in range(len(args[i])):
            vartest = args[i][j]
            vartest2 = len(args[i])
            vartest3 = len(args)
            if args[i][j] == 'X':
                perimeter += 4
                if i >= 1 and args[i][j] == args[i-1][j]:  # Tests to above, can't be less than 0 to min value is 1
                    perimeter -= 1
                if i <= (len(args)-2) and args[i][j] == args[i+1][j]:  # Tests to below, can't be larger than last index of list minus 1
                    perimeter -= 1
                if j > 0 and args[i][j] == args[i][j-1]:  # Tests left can't be first index (0)
                    perimeter -= 1
                if j <= (len(args[i])-2) and args[i][j] == args[i][j+1]:  # Tests to the right, highest is second to last max index
                    perimeter -= 1
    res = f'This is the perimeter: {perimeter}' + "'"
    return res

if __name__ == '__main__':
    #print(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"])), #"Total land perimeter: 60")
    #land_perimeter(["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]), #"Total land perimeter: 52")
    print(land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"])) #, Total land perimeter: 40")
    print(land_perimeter(["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"])), #Total land perimeter: 54")
    print(land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"])), #Total land perimeter: 40")




