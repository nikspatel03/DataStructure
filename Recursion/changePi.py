"""

Given a string, compute recursively (no loops) a new string where all
appearances of "pi" have been replaced by "3.14".

changePi("xpix") → "x3.14x"
changePi("pipi") → "3.143.14"
changePi("pip") → "3.14p"

"""
def changePi(s):
    if len(s) < 1:
        return s
    elif s[-2:] == "pi":
        return changePi(s[:-2]) + str(3.14)
    else:
        return changePi(s[:-1]) + s[-1]


print(changePi("xpiy"))
#print(changePi("pipi"))
print(changePi("pip"))
