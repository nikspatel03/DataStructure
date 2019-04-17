from Node import *

class OrderedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        newNode = Node(item)

        if self.head == None or item < self.head.getData():
            newNode.setNext(self.head)
            self.head = newNode
            return

        current = self.head
        prev = None

        while current != None:
            if current.getData() > item:
                newNode.setNext(current)
                prev.setNext(newNode)
                return
            else:
                prev = current
                current = current.getNext()


    def printList(self):
        current = self.head

        while current != None:
            print(current.getData())
            current = current.getNext()



ol = OrderedList()
ol.add(20)
ol.add(10)
ol.add(13)
ol.add(15)
ol.add(1)
ol.add(100)
ol.printList()
