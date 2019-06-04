class MaxHeap:

    def __init__(self):
        self.heaplist = [0]
        self.currSize = 0

    def insert(self, item):
        self.heaplist.append(item)
        self.currSize += 1
        self.precUp(self.currSize)

    def precUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i] > self.heaplist[i // 2]:
                self.heaplist[i], self.heaplist[i // 2] = self.heaplist[i // 2],\
                    self.heaplist[i]
            i = i // 2

    def deleteMax(self):
        item = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currSize]
        self.heaplist.pop()
        self.currSize -= 1
        self.precDown(1)
        return item

    def precDown(self, i):
        while (i * 2) <= self.currSize:
            mc = self.getMaxChild(i)
            if self.heaplist[i] < self.heaplist[mc]:
                self.heaplist[i], self.heaplist[mc] = self.heaplist[mc], \
                    self.heaplist[i]
            i = mc

    def getMaxChild(self, i):
        if (i*2) + 1 > self.currSize:
            return (i*2)
        else:
            if self.heaplist[i*2] > self.heaplist[(i*2) + 1]:
                return (i*2)
            else:
                return (i*2) + 1


maxHeap = MaxHeap()

maxHeap.insert(25)
maxHeap.insert(34)
maxHeap.insert(15)
maxHeap.insert(55)
maxHeap.insert(65)
maxHeap.insert(73)
maxHeap.insert(22)

print(maxHeap.heaplist)

print("deleted= ", maxHeap.deleteMax())
print("deleted= ", maxHeap.deleteMax())

print(maxHeap.heaplist)
