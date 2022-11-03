"""
https://www.codewars.com/kata/62f7ca8a3afaff005669625a
"""

def pyramid(h):
    if h == 1:
        return 5, 6
    t, s, c = 0, 0, h*2-1
    while c > 1:
        s += 8*c-4
        print(s)
        t += 6*c**2
        c-=2
    return (5 + 20*h + (1/2)*(h*(h-1)), t+6)

if __name__ == '__main__':
    print(pyramid(2))
