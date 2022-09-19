from collections import Counter

def mix2(s1, s2):
    c1, c2 = [Counter({s: n for s, n in Counter(c).items() if n > 1 and s.islower()}) for c in (s1, s2)]
    print(c1)
    print(c2)
    return '/'.join(c + ':' + -n * s for n, c, s in
                    sorted((-n, '=12'[(c1[s] == n) - (c2[s] == n)], s) for s, n in (c1 | c2).items()))

listtest: list = "abcasdfasdfasdfasdfa"

testval2 = [123, 123, 123]
d: Counter = Counter(testval2)
d.most_common(1)

c = Counter(listtest).items()

if __name__ == "__main__":
    t1, t2 = "looping is fun but dangerous", "less dangerous than coding"
    mix2(t1, t2)