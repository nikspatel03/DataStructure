"""
Given a string, compute recursively a new string where all the adjacent chars
are now separated by a "*".

allStar("hello") → "h*e*l*l*o"
allStar("abc") → "a*b*c"
allStar("ab") → "a*b"

"""

def allStar(s):
    if len(s) <= 1:
        return s
    else:
        return s[0] + "*" + allStar(s[1:])

print(allStar("hello"))
print(allStar("abc"))
print(allStar("ab"))
