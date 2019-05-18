"""

Given a string, compute recursively (no loops) the number of "11" substrings in
the string. The "11" substrings should not overlap.


count11("11abc11") → 2
count11("abc11x11x11") → 3
count11("111") → 1
"""


def count11(s):
    if len(s) < 2:
        return 0
    else:
        return 1 + count11(s[2:]) if s[:2] == "11" else count11(s[1:])


print(count11("11abc11"))
print(count11("abc11x11x11"))
print(count11("111"))
