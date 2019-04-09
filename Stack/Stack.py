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


def revstring(mystr):
    s = Stack()
    newList = []
    input = list(mystr)
    for x in input:
        s.push(x)
    while not s.isEmpty():
        newList.append(s.pop())
    return ''.join(newList)

print(revstring("hello"))
