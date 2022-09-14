# TEST NUMBER - 1964827

beginnum = 0
counter = 0
def recurseit(num):
    global counter
    global beginnum
    if counter == 0:
        beginnum = num
        counter += 1
    else:
        thisnum = str(num)
        firsthalf = thisnum[:len(thisnum)-2]
        toplevel_placecount = 2
        secondhalf = thisnum[:-toplevel_placecount]

        def innerrecurse(firsthalf, secondhalf):




