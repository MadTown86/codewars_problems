"""
Find maximum subarray within array - values remain in order

Test Case #1: ([-2, 1, -3, 4, -1, 2, 1, -5, 4])

Test C

Logic Case1 - turn list into sum pairs to see for larger values
-> [-1, 1, 1, 0]

Logic Case2 - iterate left to right, pairwise, slicing off pairs that give negative values:

Logic Case3 - 

simple for loop, single direction, not necessary to check backwards
mark the beginning and end of the sequence that will result in the highest summed value
"""
import itertools
testcase1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
incl = [0]
for ind, val in enumerate(testcase1):
    if ind < len(testcase1)-1:
        if testcase1[ind+1] > val or testcase1[ind+1] > 0:
            incl.append(1)
        else:
            incl.append(0)

markerpos = []
markerneg = []
increasing = []
decreasing = []
runtot = 0
for x, value in enumerate(testcase1):
    # Mark head or tail as pos/neg markers
    # if value >= 0 and x == 0:
    #     markerpos.append(x)
    # elif value < 0 and x == 0:
    #     markerneg.append(x)
    # if value >= 0 and x == len(testcase1)-1:
    #     markerpos.append(x)
    # elif value < 0 and x == len(testcase1)-1:
    #     markerneg.append(x)

    #Loop calc total, mark points where total turns neg or pos
    if x != len(testcase1)-1:
        last_runtot = runtot
        runtot += value

    if last_runtot > runtot:
        decreasing.append(x)
    else:
        increasing.append(x)


    if last_runtot < 0 and runtot >= 0:
        markerpos.append(x)
    elif last_runtot > 0 and runtot <= 0:
        markerneg.append(x)

print(f'TESTCASE: {testcase1}')
print(f'INCL: {incl}')
print(f'POS: {markerpos}')
print(f'INCREASING: {increasing}')
print(f'NEG: {markerneg}')
print(f'DECREASING: {decreasing}')

testcase1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


"""
I want to check through each set of values
list of comparisons I need to make:
1. last value as compared to current value
2. last sum as compared to current sum
3. When sum turns positive or negative

What I am trying to do:
Iterate through list, comparing both item and sum of sublist to the 
current item and current sum of sublist with updated tail respectively.

Find first summation of pairs that creates a positive number and relocate head at this position
then continually move tail out until you reach a negative sum, storing highest summed head/tail pair along the way

"""

testcase1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# head move case: if sum negative, if new sum > old sum
# Tail move case: while sum > 0 increment tail forward
# Track highest case - log highest head/tail sum

def maxarrgylesocks(arr):
    head_tail = []
    cur_highest = 0
    for ind, curvalue in enumerate(arr):
        #Initial setup
        if ind == 0:
            lastval = curvalue
            runsum = curvalue
            head = ind
            tail = ind + 1
            logsum = sum(arr[head:tail])
        else:
            #Head Movement case
            lastsum = runsum
            runsum += curvalue
            if lastsum < runsum and lastsum < 0 and runsum >= 0:
                head = ind
                tail = ind + 1
                runsum = curvalue
            # Tail move case
            elif runsum > 0:
                tail = ind
                logsum = sum(arr[head:tail])
                if logsum > cur_highest:
                    cur_highest = logsum
                    head_tail = [head, tail]

    return arr[head_tail[0]:head_tail[1]]

print(maxarrgylesocks(testcase1))


            
            




        

        





