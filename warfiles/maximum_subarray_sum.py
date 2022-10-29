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
complexcase = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]

incorrect1 = [24, 22, -2, 31, -16, 27, 36, 16, -21, -2, -26, -34, 17, 27, -34, 16, 34, 23, 3, 2, 16, 36, -27, 24, -38, -40, 40, 24, 33, 18, 13, 24, 26, -35, 23, -2, -36, 24, 29, 13, 9, -18]
#317
incorrect2 = [18, 23, -8, 15, 32, -5, 17, 8, -29, -24, 30, 22, 3, -25, 17, 2, 17, -24, 22, 0, 19, -7, 32, -24, -32, 21, 32, 17, -21]
#169


#Two possible outlier cases I haven't considered:
# individual values being higher than the highest sum
# head move case: if sum negative, if new sum > old sum
# Tail move case: while sum > 0 increment tail forward
# Track highest case - log highest head/tail sum

"""
def max_sequence(arr):
    if arr:
        if min(arr) > 0:
            return sum(arr)
        elif max(arr) < 0:
            return 0
        else:
            head_tail = []
            cur_highest = 0
            for ind, curvalue in enumerate(arr):
                #Initial setup
                if ind == 0:
                    runsum = curvalue
                    head = ind
                    tail = ind + 1
                    logsum = sum(arr[head:tail])
                else:
                    #Head Movement case
                    lastsum = runsum
                    runsum += curvalue
                    if lastsum < runsum and lastsum < 0:
                        head = ind
                        tail = ind + 1
                        runsum = curvalue
                    # Tail move case
                    elif runsum > 0:
                        tail = ind
                        if ind != len(arr)-1:
                            logsum = sum(arr[head:tail])
                        else:
                            logsum = sum(arr[head:])
                        if logsum > cur_highest:
                            cur_highest = logsum
                            head_tail = [head, tail]
                        if curvalue > cur_highest:
                            cur_highest = curvalue
                    elif runsum < 0:
                        continue

            if head_tail[1] == len(arr)-1:
                return sum(arr[head_tail[0]:])
            else:
                return sum(arr[head_tail[0]:head_tail[1]])
    else:
        return 0

print(max_sequence(complexcase))

Works for most test cases but is garbage

"""
testcase1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
complexcase = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]

incorrect1 = [24, 22, -2, 31, -16, 27, 36, 16, -21, -2, -26, -34, 17, 27, -34, 16, 34, 23, 3, 2, 16, 36, -27, 24, -38, -40, 40, 24, 33, 18, 13, 24, 26, -35, 23, -2, -36, 24, 29, 13, 9, -18]
#317
incorrect2 = [18, 23, -8, 15, 32, -5, 17, 8, -29, -24, 30, 22, 3, -25, 17, 2, 17, -24, 22, 0, 19, -7, 32, -24, -32, 21, 32, 17, -21]
#169

def max_sequence(arr):
    highest_sum = 0
    if arr:
        if min(arr) > 0:
            return sum(arr)
        elif max(arr) < 0:
            return 0
        else:
            runsum = 0
            # begin search for paradise
            for curvalue in arr:
                lastsum = runsum
                runsum += curvalue
                if runsum > highest_sum:
                    highest_sum = runsum
                if runsum > lastsum and lastsum <= 0 and curvalue >= 0:
                    runsum = curvalue
                    head = curvalue

            return highest_sum
    else:
        return 0
        
print(max_sequence(incorrect2))

"""
lollerskates quite a lot of unnecessary garbage

Top Answer:

def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max

Comments:************************
    # I didn't think to simply reset the current number to zero every time it dropped below zero.
    A lot boils down to how you can conceptualize the problem statement and visualize ways of solving it.

    Also making sure that you truly understand what is being asked and only solve for that and not a bunch of other
    things.
***********************
Other Unique:

"""




        

        





