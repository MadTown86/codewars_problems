import itertools

def next_bigger(num):
    local_num = str(num)
    first_digit = local_num[:1]  # Saving First Digit
    local_minus_first = local_num[1:]

    # Outlier case #1 - all same digit
    if local_num.count(first_digit) == len(local_num):
        return -1


    # Outlier case #2 - 2 digits
    if len(local_num) == 2:
        if local_num[:1] >= local_num[1:]:
            return -1
        else:
            return int((local_num[1:] + local_num[:1]))

    else:
        dcount_floop = 2  # Establish Digit Counter

    # Begin looping through digits right to len(num) -1, test if next bigger can be found else continue
    while dcount_floop <= len(local_num):
        front = local_num[:-dcount_floop]
        original_back = local_num[-dcount_floop:]
        original_back_firstdigit = original_back[0]

        if "".join(sorted(original_back, reverse=True)) > original_back:

            higher_listchunk = sorted(original_back, reverse=True)
            difference_list = [int(x) - int(original_back_firstdigit) for x in higher_listchunk]
            sort_dif_list = sorted(difference_list)
            for x in sort_dif_list:
                if x > 0:
                    new_first_digit = higher_listchunk[difference_list.index(x)]
                    higher_listchunk.remove(new_first_digit)
                    sort_higher_listchunk = sorted(higher_listchunk)
                    next_highest = "".join(itertools.chain(new_first_digit, sort_higher_listchunk))
                    new_while_result = front + next_highest
                    return int(new_while_result)
        else:
            dcount_floop += 1
            continue

    return -1