"""
Given a string, compute recursively the number of times lowercase "hi" appears
in the string, however do not count "hi" that have an 'x' immedately before
them.

countHi2("ahixhi") → 1
countHi2("ahibhi") → 2
countHi2("xhixhi") → 0

"""

def countHi2(s):
    if len(s) < 3:
        return 0
    else:
        return 1 + countHi2(s[1:]) if (s[0] != 'x' and s[1:3] == 'hi') else countHi2(s[1:])


print(countHi2("ahixhi"))
print(countHi2("ahibhi"))
print(countHi2("xhixhi"))
print(countHi2("hihihix"))
