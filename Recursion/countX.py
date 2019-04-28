"""
Given a string, compute recursively (no loops) the number of lowercase 'x' chars
in the string.


countX("xxhixx") → 4
countX("xhixhix") → 3
countX("hi") → 0

"""

def countX(str):
    if len(str) == 0:
        return 0
    if str[0] == 'x':
        return 1 + countX(str[1:])
    else:
        return countX(str[1:])

print(countX("xxhixx"))
print(countX("xhixhix"))
print(countX("hihellox"))
print(len(""))

s = "a"
print(s[0])
print(len(s[1:]))


"""
if str[0] == 'x':
    return 1 if str == "x" else 0
else:
    return 1 + countX(str[1:]) if str[0] == "x" else 0 + countX(str[1:])
"""
