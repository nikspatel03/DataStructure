"""
Given a string, compute recursively (no loops) the number of times lowercase
"hi" appears in the string.

countHi("xxhixx") → 1
countHi("xhixhix") → 2
countHi("hi") → 1

"""

def countHi(s):
    if len(s) < 2:
        return 0
    else:
        return 1 + countHi(s[:-1]) if s[-2:] == "hi" else countHi(s[:-1])


print(countHi("xxhixx"))
print(countHi("xhixhix"))
print(countHi("hi"))
