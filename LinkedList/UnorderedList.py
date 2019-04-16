# implementation of Unordered LinkedList
from Node import *

class UnorderedList:

    def __init__(self):
        self.head = None


    def isEmpty():
        return self.head == None


    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp


    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count


    def search(self, item):
        current = self.head
        isFound = False
        while current != None and not isFound:
            if current.getData() == item:
                isFound = True
            else:
                current = current.getNext()

        return isFound

    def remove(self, item):

        # Case : When head to be removed
        if(self.head.getData() == item):
            self.head = self.head.getNext()

        current = self.head

        while current.getNext() != None and current.getNext().getNext() != None:
            if current.getNext().getData() == item:
                current.setNext(current.getNext().getNext())
            else:
                current.setNext(current.getNext())

        if current.getNext().getData() == item:
            current.setNext(current.getNext().getNext())
        else:
            return 100

ul = UnorderedList()

ul.add(10)
ul.add(11)
ul.add(12)
ul.add(13)
ul.add(14)
ul.add(15)

print(ul.size())
print(ul.search(115))

ul.remove(10)
print(ul.size())
