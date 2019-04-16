# Implementation of Dequeue abstract data structure

class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

d=Deque()
print(d.isEmpty())
d.addRear(4)
d.addRear('dog')
d.addFront('cat')
d.addFront(True)
print(d.size())
print(d.isEmpty())
d.addRear(8.4)
print(d.removeRear())
print(d.removeFront())



def palchecker(aString):
    d = Deque()
    for ch in aString:
        d.addRear(ch)
    isPalindrome = True
    while d.size() > 1 and isPalindrome:
        if d.removeRear() != d.removeFront():
            isPalindrome = False
    return isPalindrome

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
