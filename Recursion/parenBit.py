"""

Given a string that contains a single pair of parenthesis, compute recursively
a new string made of only of the parenthesis and their contents,
so "xyz(abc)123" yields "(abc)".

parenBit("xyz(abc)123") → "(abc)"
parenBit("x(hello)") → "(hello)"
parenBit("(xy)1") → "(xy)"

"""

def parenBit(s):
    return _parentBitHelper(s, False)

def _parentBitHelper(s, flag):
    if len(s) < 1:
        return s
    elif s[0] == "(":
        flag = True
    elif s[0] == ")":
        flag = False

    return s[0] + _parentBitHelper(s[1:], flag) if (flag is True or s[0] == ")") else _parentBitHelper(s[1:], flag)


print(parenBit("ab(ab)ab"))
print(parenBit("hello(not really)there"))
print(parenBit("(x)"))
print(parenBit("(abc)x"))
