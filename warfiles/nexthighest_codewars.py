# 1234567321
# 15065330
# 15065330
import itertools

def next_bigger(num):
    """
    1. Test outlier conditions
    2. Loop through digits from right to left, using sort to check if potential new highest
    3. Loop only checks up to second highest place digit, create algorithm to check for next largest highest place value
    """

    local_num = str(num)

    # Outlier cases - 2 digits
    if len(local_num) == 2:
        if local_num[:1] >= local_num[1:]:
            return -1
        else:
            return int((local_num[1:] + local_num[:1]))

    else:
        dcount_floop = 2

    while dcount_floop < len(local_num):
        front = local_num[:-dcount_floop]
        original_back = local_num[-dcount_floop:]


        # This bit is not True for following setup: 67321 sorted returns 76---, need 71---
        if "".join(sorted(original_back, reverse=True)) > original_back:
            higher_listchunk = sorted(original_back, reverse=True)
            higher_firstdigit = higher_listchunk.pop(0)
            sort_higher_listchunk = sorted(higher_listchunk)
            next_highest = "".join(itertools.chain(higher_firstdigit, sort_higher_listchunk))
        else:
            continue










if __name__ == "__main__":
    # print(next_bigger(1234567908))
    # print(next_bigger(59483726))
    # print(next_bigger(9876789))
    # print(next_bigger(1357642))
    print(next_bigger2(890123683457))  # 890123683457
