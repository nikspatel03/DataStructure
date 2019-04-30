"""
Given a string, compute recursively (no loops) a new string where all the
lowercase 'x' chars have been changed to 'y' chars.

changeXY("codex") → "codey"
changeXY("xxhixx") → "yyhiyy"
changeXY("xhixhix") → "yhiyhiy"

"""

def changeXY(s):
    res = ""
    if len(s) < 1:
        return s
    else:
        ch = s[0]
        if ch == 'x':
            return 'y' + changeXY(s[1:])
        else:
            return ch + changeXY(s[1:])

print(changeXY("codex"))
print(changeXY("xxhixx"))
print(changeXY("xhixhix"))
