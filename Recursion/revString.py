"""
Reverse String using recursion




def revString(myStr):
    if len(myStr) <= 1:
        return myStr
    else:
        return myStr[-1] + revString(myStr[0:-1])
"""

def revString(myStr):
    if len(myStr) == 0:
        return myStr
    else:
        return revString(myStr[1:]) + myStr[0]

print(revString("hello"))
print(revString("abc"))
print(revString(""))
print(revString("abcde"))
