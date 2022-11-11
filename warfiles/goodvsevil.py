"""
https://www.codewars.com/kata/52761ee4cffbc69732000738
"""



good_power = [1, 2, 3, 3, 4, 10]
evil_power = [1, 2, 2, 2, 3, 5, 10]

def good_vs_evil(good, evil):
    gpow = 0
    bpow = 0

    for pow, race in zip(good_power, [int(x) for x in good.split(" ")]):
        gpow += pow*race

    for pow, race in zip(evil_power, [int(x) for x in evil.split(" ")]):
        bpow += pow*race

    print(gpow, bpow)

    if gpow > bpow:
        return 'Battle Result: Good triumphs over Evil'
    elif gpow == bpow:
        return 'Battle Result: No victor on this battle field'
    else:
        return 'Battle Result: Evil eradicates all trace of Good'

test = '1 1 1 1 1 1', '1 1 1 1 1 1 1'

if __name__ == "__main__":
    good_vs_evil(*test)