"""
Stack implementation in Python
"""
import os, sys
sys.path.insert(0,"/Users/nikul.g.patel/github/DataStructure")

from test import *
import string

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


testEqual(revstring("hello"),'olleh')

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


testEqual(parChecker('(()'),False)
testEqual(parChecker('((()))'),True)

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

testEqual(generalParChecker('{{([][])}()}'),True)
testEqual(generalParChecker('[{()]'),False)

def divideBy2(decimalNum):
    remStack = Stack()
    while decimalNum > 0:
        rem = decimalNum % 2
        remStack.push(rem)
        decimalNum = decimalNum // 2

    binStr = ""
    while not remStack.isEmpty():
        binStr = binStr + str(remStack.pop())

    return binStr


#print(divideBy2(43))

testEqual(divideBy2(43),"101011")
testEqual(divideBy2(10),"1010")
testEqual(divideBy2(233),"11101001")



def baseConverter(decNumber,base):
    remStack = Stack()
    digits = "0123456789ABCDEF"

    while decNumber > 0:
        rem = decNumber % base
        remStack.push(rem)
        decNumber = decNumber // base

    retStr = ""
    while not remStack.isEmpty():
        retStr = retStr + digits[remStack.pop()]

    return retStr


testEqual(baseConverter(25,2),"11001")
testEqual(baseConverter(10,2),"1010")
testEqual(baseConverter(25,16),"19")


def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postfixStr = ""

    for ch in infixexpr:
        if (ch in string.ascii_letters) or (ch in string.digits):
            postfixStr = postfixStr + ch
        elif ch == "(":
            opStack.push(ch)
        elif ch == ")":
            top = opStack.pop()
            while top != "(":
                postfixStr = postfixStr + top
                top = opStack.pop()
        else:
            while(not opStack.isEmpty() and prec[opStack.peek()] >= prec[ch]):
                postfixStr = postfixStr + opStack.pop()
            opStack.push(ch)

    while (not opStack.isEmpty()):
        postfixStr = postfixStr + opStack.pop()

    return postfixStr

print(infixToPostfix("A*B+C*D"))
print(infixToPostfix("(A+B)*C-(D-E)*(F+G)"))


def postfixEval(postfixExpr):
    opStack = Stack()

    for ch in postfixExpr:
        if ch in string.digits:
            opStack.push(int(ch))
        else:
            op2 = opStack.pop()
            op1 = opStack.pop()
            res = doMath(ch, op1, op2)
            opStack.push(res)

    return opStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


print(postfixEval("456*+"))
