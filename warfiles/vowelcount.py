"""
https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
"""

def get_count(sentence):
    return sum([sentence.count(char) for char in ['a', 'e', 'i', 'o', 'u']])

name = 'crap'
name2 = 'rob'
def playingbanjo(stname):
    return stname + " plays banjo" if stname[0].lower() == 'r' else stname + " does not play banjo"

if __name__ == "__main__":
    print(playingbanjo(name2))