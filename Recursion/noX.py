"""
Given a string, compute recursively a new string where all the 'x' chars have
been removed.

noX("xaxb") → "ab"
noX("abc") → "abc"
noX("xx") → ""

"""

def noX(s):
    if len(s) < 1:
        return s
    else:
        return noX(s[:-1]) if s[-1] == "x" else noX(s[:-1]) + s[-1]

print(noX("xaxb"))
print(noX("abc"))
print(noX("xx"))  
