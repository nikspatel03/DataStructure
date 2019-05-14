"""
Count recursively the total number of "abc" and "aba"
substrings that appear in the given string.

countAbc("abc") → 1
countAbc("abcxxabc") → 2
countAbc("abaxxaba") → 2
"""


def countAbc(s):
    if len(s) < 3:
        return 0
    else:
        return 1 + countAbc(s[1:]) if s[0:3] == "abc" or s[0:3] == "aba" \
                else countAbc(s[1:])


print(countAbc("abc"))
print(countAbc("abcxxabc"))
print(countAbc("abaxxaba"))
print(countAbc("abx"))
