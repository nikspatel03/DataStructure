"""
Given a string, return recursively a "cleaned" string where adjacent chars
that are the same have been reduced to a single char. So "yyzzza" yields "yza".


stringClean("yyzzza") → "yza"
stringClean("abbbcdd") → "abcd"
stringClean("Hello") → "Helo"


"""

def stringClean(s):
    if len(s) < 2:
        return s
    else:
        return s[0] + stringClean(s[1:]) if s[0] != s[1] else stringClean(s[1:])


print(stringClean("yyzzza"))
print(stringClean("abbbcdd"))
print(stringClean("Hello"))
