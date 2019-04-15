# implementation of abstract datatype Queue

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()

q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)

print(q.size())

print(q.isEmpty())

q.enqueue(8.4)
print(q.dequeue())
print(q.dequeue())
print(q.size())



def hotPotato(namelist, num):
    q = Queue()
    for name in namelist:
        q.enqueue(name)
    while q.size() > 1:
        for i in range(0,num):
            name = q.dequeue()
            q.enqueue(name)
        q.dequeue()

    return q.dequeue()


print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
