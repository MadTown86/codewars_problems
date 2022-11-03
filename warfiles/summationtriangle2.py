"""
Double subscript notation:
X_ij - row/column potential

If the subscript goes above nine elements you can see a space between i, j a comma or braces around the numbers

https://www.statpower.net/Content/310/Summation%20Algebra.pdf



Pay attention to where the parethesis are, if the parenthesis are around the equation and not the summation symbol
then you sum the results of the equations.  Not, say, perform an action with the entire sum.

However, for addition, because the result would be the same, the entire summation symbol may simply be used for the
addition of one series to another.

c or k's in the summation notion usually refer to a constant.

Summation Algebra Rules
1. The first constant rule (a = (y - x + 1)a) y is the stop value, i = x is the start value - remember off by 1
    - or (N * a)
    - (A) stands for ANY constant algebraic function that does not change as a result to the incrementation of i
    -Multiplication is simply repeated addition
    -Learn more about s ummation notation to understand this
2. Second Constant Rule (8 * (x + y + z)) = (8x + 8y + 8z)  (you can factor a common divisor as well
    -You can remove a factorable constant out of the summation operator
    -It can also stand for a factorable divisor or a fraction that can be removed and multiplied to the whole series
3. The distributive rule
    - Basically, if one has two functions for which you are adding together their resultant series, you can separate them out
    algebraically and add them together as two separate summation equations. E(x - y) == Ex - Ey (or the addition equiv)

Some key notations to remember:
sample mean looks like an x with a line over it and a solid subscript dot

Deviation score looks like [dx]_i = x_i - sample mean

An apostrophe in an equation like " k' " means a permutation of that equation

"""


def get_sum_buildingtriangle(n):
    if n == 0:
        return 1
    row, col = 0, 0

    equation = lambda row, col: (2 * row + col + 1) * ((-1) ** (2 * row + col))
    tri_sum = 0

    def rowcur(n, row, col, colm):
        templ = []
        if colm > col:
            col += 1
            return rowcur(n, row, col, colm)
        if col == n + 1:
            return []
        else:
            templ.append(equation(row, col))
            col += 1
            return templ + rowcur(n, row, col, colm)

    colm = -1
    while row < n + 1:
        row_list = []
        row_list.append(rowcur(n, row, col, colm))
        tri_sum += sum(row_list[0])
        row += 1
        colm = row

    return tri_sum

if __name__ == "__main__":
    import math
    tempbin = []
    argbin = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for x in argbin:
        tempbin.append(get_sum_buildingtriangle(x))
    newbin3 = list(map(lambda x, y: abs(x) - abs(y), tempbin[:-1], tempbin[1:]))
    newbin4 = list(map(lambda x, y: x - y, newbin3[:-1], newbin3[1:]))
    newbin5 = list(map(lambda x, y: x - y, newbin4[:-1], newbin4[1:]))
    newbin6 = list(map(lambda x, y: x - y, newbin5[:-1], newbin5[1:]))
    newbin7 = list(map(lambda x, y: x - y, newbin6[:-1], newbin6[1:]))
    newbin8 = list(map(lambda x, y: x - y, newbin7[:-1], newbin7[1:]))
    newbin9 = list(map(lambda x, y: x - y, newbin8[:-1], newbin8[1:]))

    print(tempbin)
    print(" " + str(newbin3))
    print("    " + str(newbin4))
    print("     " + str(newbin5))
    print("         " + str(newbin6))
    print("            " + str(newbin7))
    print("               " + str(newbin8))
    print("                  " + str(newbin9))