"""
Given a string, compute recursively a new string where all the lowercase 'x'
chars have been moved to the end of the string.

endX("xxre") → "rexx"
endX("xxhixx") → "hixxxx"
endX("xhixhix") → "hihixxx"

"""
def endX(s):
    if len(s) < 1:
        return s
    else:
        return s[0] + endX(s[1:]) if s[0] != 'x' else endX(s[1:]) + s[0]

print(endX("xxre"))
print(endX("xxhixx"))
print(endX("xhixhix"))
print(endX("x"))
