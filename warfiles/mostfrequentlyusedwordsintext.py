from collections import defaultdict
import heapq

"""
https://www.codewars.com/kata/51e056fe544cf36c410000fb/python
"""

# Old Way - Trying to go straight parse string to answer instead of alter string -> list -> sort answer

# tempdict = {}
# for char in samplequote:
#     if char in string.lower():
#         firstind = sample

# def top_3_words(text: str) -> list[str]:
#     if len(text) == 0:
#         return []
#     else:
#         # Clean input
#         def cleanit(text):
#             import string
#             chbin = string.punctuation
#             chbin = chbin.replace("'", '')
#             text = text.lower()
#             text = '%r' % ''.join(text)
#             text = text.replace('\\n', ' ')

#             for char in chbin:
#                 text = text.replace(char, "")


#             ctext = text.split(" ")

#             # othbin = ["'", "''", '"', '""']
#             # for chars in othbin:
#             #     if chars in ctext:
#             #         ctext.remove(chars)

#             ctextd = ctext
#             while '' in ctextd:
#                 for x in ctextd:
#                     if len(x) == 0:
#                         ctextd.remove(x)

#             print(ctextd)
#             return ctextd

#         # Count, remove, store highest three
#         def countit(ctext: list, clist: dict, hnum: list) -> (dict, list):
#             if not ctext:
#                 return clist
#             else:
#                 for item in ctext:
#                     if item in clist.keys():
#                         continue
#                     else:
#                         c = ctext.count(item)
#                         # Trickle down highest as you go
#                         if c > hnum[0]:
#                             hnum[2] = hnum[1]
#                             hnum[1] = hnum[0]
#                             hnum[0] = c
#                             clist[item] = c
#                             ctext.remove(item)
#                         elif hnum[1] < c < hnum[0]:
#                             hnum[2] = hnum[1]
#                             hnum[1] = c
#                             clist[item] = c
#                             ctext.remove(item)
#                         elif hnum[2] < c < hnum[1]:
#                             hnum[2] = c
#                             clist[item] = c
#                             ctext.remove(item)
#                         else:
#                             continue
#                     countit(ctext, clist, hnum)

#             return (clist, hnum)

#         # Filter for 3 highest
#         def filterit(clist: dict, hnum: list) -> list:
#             outlist = []
#             for val in hnum:
#                 if val > 0:
#                     for ind, num in enumerate(clist.values()):
#                         if num == val:
#                             outlist.append([x for x in clist.keys()][ind])
#             return outlist


#         clist = {}
#         hnum = [0, 0, 0]

#         return filterit(*countit(cleanit(text), clist, hnum))

samplequote = """
In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""

def top_3_words(text):
    word = ""
    dictpack = defaultdict(int)
    for char in text:
        if char.isalpha() or char == "'":
            word += char
        else:
            if word == "":
                continue
            else:
                dictpack[word] += 1
                word = ""
    
    output = []

    for key, value in dictpack.items():
        heapq.heappush(output, (value, key))
        if len(output) > 3:
            heapq.heappop(output)
    
    print(output)
            
    
    



if __name__ == "__main__":
    print(top_3_words(samplequote))
    # print(top_3_words(""))
    # print(top_3_words("e e e e"))
    # print(top_3_words("   e   ,  "))
    # print(top_3_words(" //wont won't won't"))