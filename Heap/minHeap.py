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


minHeap = MinHeap()

minHeap.insert(5)
minHeap.insert(188)
minHeap.insert(9)
minHeap.insert(2)
minHeap.insert(1)


print(minHeap.heapList)
