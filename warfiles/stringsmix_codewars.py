"""
4 kyu
import codewars_test as test
from solution import mix

@test.describe("Mix")
def _():
    @test.it("Basic Tests")
    def _():
        test.assert_equals(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
        test.assert_equals(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp"), '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
        test.assert_equals(mix("looping is fun but dangerous", "less dangerous than coding"), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
        test.assert_equals(mix(" In many languages", " there's a pair of functions"), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
        test.assert_equals(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
        test.assert_equals(mix("codewars", "codewars"), "")
        test.assert_equals(mix("A generation must confront the looming ", "codewarrs"), "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")

 If firstchar count in answer, ans += '1:char*n'



passed the first few test garbages:

Failed the following:

'1:ooo/1:sss/2:bbb/1:--/1:nn/1:uu/1:ww/2:aa/2:cc/2:dd/2:ff/2:xx' should equal '1:ooo/1:sss/2:bbb/1:nn/1:uu/1:ww/2:aa/2:cc/2:dd/2:ff/2:xx'
'1:eee/1:dd/1:hh/1:ll/1:rr/1:ss/2:RR/2:ii/2:mm/2:nn/2:zz/=:aa' should equal '1:eee/1:dd/1:hh/1:ll/1:rr/1:ss/2:ii/2:mm/2:nn/2:zz/=:aa'
'1:kkkk/1:yyy/2:nnn/1:KK/1:rr/1:ww/1:zz/2:dd/2:gg/2:ii/2:jj/2:uu' should equal '1:kkkk/1:yyy/2:nnn/1:rr/1:ww/1:zz/2:dd/2:gg/2:ii/2:jj/2:uu'



*MOST LIKED ANSWER:

def mix(s1, s2):
    hist = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            which = "1" if val1 > val2 else "2" if val2 > val1 else "="
            hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
    return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))
"""
import string
from collections import defaultdict
import itertools



def mix(s1: str, s2: str):

    tempval_char: str = ""
    tempval_char2: str = ""

    bin_capital = [x for x in itertools.chain(string.ascii_uppercase, string.punctuation)]
    for upper in bin_capital:
        s1 = s1.replace(upper, "")
        s2 = s2.replace(upper, "")

    dict1: dict = {}
    dict2: dict = {}
    # This section cleans the string, removes uppercase and spaces and removes any chars with count == 1


    s1r = s1.strip(string.ascii_uppercase).replace(" ", "")

    for char in s1r:
        if char.isupper():
            print("IS UPPER:  ", char)
    s1r = s1r.strip(string.ascii_uppercase)
    for char in s1r:
        if s1r.count(char) == 1:
            s1r = s1r.replace(char, "")
            s1r = "".join(sorted(s1r))
        if char in dict1.keys():  # Creating a string to house 'COUNT'+'char'
            continue
        elif s1r.count(char) > 1:
            dict1[str(char)] = str(s1r.count(char))

    # This section does the same as above for the second string
    s2r = s2.strip(string.ascii_uppercase).replace(" ", "")
    s2r = s2r.strip(string.ascii_uppercase)
    for char in s2r:
        if s2r.count(char) == 1:
            s2r = s2r.replace(char, "")
            s2r = "".join(sorted(s2r))
        if char in dict2.keys():
            continue
        elif s2r.count(char) > 1:
            dict2[str(char)] = str(s2r.count(char))

            # Update dictionary with dict[COUNT] = char format, check if duplicate and overwrite with higher val_charue
    outputdict: dict = {}
    for key, val_charue in dict1.items():
        if key in dict2.keys():
            val_charue2nd = dict2[key]
            if val_charue > val_charue2nd:
                outputdict[key] = val_charue
            else:
                outputdict[key] = val_charue2nd
        else:
            outputdict[key] = val_charue

    for key, val_charue in dict2.items():
        if key not in outputdict.keys():
            outputdict[key] = val_charue

    # Original list of keys/val_charues for indexing to dictionary by val_charue
    outputdict_val_charues = [val_char for val_char in outputdict.values()]
    outputdict_keys = [key for key in outputdict.keys()]

    # Grouping dictionary with defaultdict/list
    outputdict_reorg: defaultdict = defaultdict(list)
    for key, val_char in sorted(outputdict.items()):
        outputdict_reorg[val_char].append(key)

    output_k: list = []
    for k, v in outputdict_reorg.items():
        output_k.append(k)
    output_k = sorted(output_k, reverse=True)

    res = ""

    for key in output_k:
        first_bin: list = []
        second_bin: list = []
        equal_bin: list = []
        for val_char in outputdict_reorg[key]:
            if val_char in dict1.keys() and val_char in dict2.keys():
                if dict1[val_char] > dict2[val_char]:
                    first_bin.append("1:" + int(key) * str(val_char) + "/")

                elif dict1[val_char] < dict2[val_char]:
                    second_bin.append("2:" + int(key) * str(val_char) + "/")

                else:
                    equal_bin.append("=:" + int(key) * str(val_char) + "/")

            elif val_char in dict1.keys():
                first_bin.append("1:" + int(key) * str(val_char) + "/")
            else:
                second_bin.append("2:" + int(key) * str(val_char) + "/")


        first_bin.sort()
        second_bin.sort()
        equal_bin.sort()
        while first_bin:
            poppedvar = first_bin.pop(0)
            res += poppedvar
        while second_bin:
            res += second_bin.pop(0)
        while equal_bin:
            res += equal_bin.pop(0)


    return res[:-1]

if __name__ == "__main__":
    t1, t2 = "looping is fun but dangerous", "less dangerous than coding"
    #res = mix(t1, t2)
    print(mix("Sadus:cpms>orqn3zeGGGvnznSGacs", "MynwdKizfd$lvse+gnbaGydxyXzayp"))

    #print(f'res: {res}')





