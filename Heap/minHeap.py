class MinHeap:

    def __init__(self):
        self.heapList = [0]
        self.curr_size = 0

    def insert(self, item):
        self.heapList.append(item)
        self.curr_size += 1
        self.precUp(self.curr_size)

    def precUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2],\
                    self.heapList[i]
            i = i // 2

    def delMin(self):
        retVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.curr_size]
        self.heapList.pop()
        self.curr_size -= 1
        self.precDown(1)
        return retVal

    def precDown(self, i):
        while (i * 2) <= self.curr_size:
            mc = self.minChild(i)

            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]

            i = mc

    def minChild(self, i):
        if (i * 2) + 1 > self.curr_size:
            return (i * 2)
        else:
            if self.heapList[(i * 2)] < self.heapList[(i * 2) + 1]:
                return (i * 2)
            else:
                return (i * 2) + 1


#minHeap = MinHeap()
bh = MinHeap()
bh.insert(5)
bh.insert(7)
bh.insert(3)
bh.insert(11)

print(bh.delMin())

print(bh.delMin())

print(bh.delMin())

print(bh.delMin())
"""
minHeap.insert(5)
minHeap.insert(188)
minHeap.insert(9)
minHeap.insert(2)
minHeap.insert(1)


print(minHeap.heapList)
print(minHeap.delMin())
print(minHeap.heapList)
"""
