"""https://www.codewars.com/kata/529bf0e9bdf7657179000008/python"""

"""
Two Ideas:
1. Naive perhaps and very large/cumbersome: reshape array into three forms package into an iterable, then loop or recurse through each set of 9
2. May be better: join into a string and loop through entire string and create checks within that one loop.
"""

# Most likely naive way.
valid_solutionl = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

import itertools

def valid_solution(arr):

    # Straight original check
    def orgcheck(arr):
        for row in arr:
            if sum(row) != 45:
                return False
        
        return True

    #col to row then check
    def ctr(arr):
        d = {}
        tempv = []

        for row in arr:
            for i, v in enumerate(row):
                if str(i) in d.keys():
                    temp = d[str(i)]
                    temp.append(v)
                    d[str(i)] = temp
                else:
                    tempv = [v]
                    d[str(i)] = tempv
        
        tolist = [sum(d[key]) for key in d.keys()]
        for item in tolist:
            if item != 45:
                return False
        
        return True

    # 9 blocks sums then check
    def tnineg(arr):
        tnc = {}
        f = [0, 3, 6]
        b = [3, 6, 9]
        for f, b in zip(f, b):
            sec = arr[f:b]
            bt1 = []
            bt2 = []
            bt3 = []
            for row in sec:
                bt1.append(row[0:3])
                bt2.append(row[3:6])
                bt3.append(row[6:9])
            tnc[str(f) + str(b)] = [bt1, bt2, bt3]
            tolist = [tnc[key] for key in tnc.keys()]

            newgobj = []
            for item in tolist:
                for i in item:
                    newgobj.append(sum([x for x in itertools.chain.from_iterable(i)]))

        for item in newgobj:
            if item != 45:
                return False
        
        return True 
    
    if orgcheck(arr) and ctr(arr) and tnineg(arr):
        return True
    
    return False


if __name__ == "__main__":
    print(valid_solution(valid_solutionl))






                    





