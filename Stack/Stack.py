"""
Stack implementation in Python
"""

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

# Reverse String function
def revstring(mystr):
    s = Stack()
    for ch in mystr:
        s.push(ch)
    revstr = ""
    while not s.isEmpty():
        revstr = revstr + s.pop()
    return revstr

print(revstring("hello"))

# Simple balance paranthses program
def parChecker(symbolStr):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolStr) and balanced:
        ch = symbolStr[index]
        if ch == "(":
            s.push(ch)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index = index + 1

    if s.isEmpty() and balanced:
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(()'))

#General case of parantheses check

def generalParChecker(symbolStr):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolStr) and balanced:
        ch = symbolStr[index]
        if ch in "({[":
            s.push(ch)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, ch):
                    balanced = False
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(top, ch):
    opening = "({["
    closing = ")}]"
    return opening.index(top) == closing.index(ch)

print(generalParChecker('{{([][])}()}'))
print(generalParChecker('[{()]'))
