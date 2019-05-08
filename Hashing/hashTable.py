"""

Implementation of HashTable abstract data structure (Python Dictionary)


"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable():

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    # Assumption: key should be str type
    def hashCode(self, astring):
        hash = 5381
        for ch in astring:
            hash = 31 * hash + ord(ch)
        return hash

    def put(self, key, value):
        hash = self.hashCode(key)
        bucket = hash % self.size
        newNode = Node(key, value)
        if not self.contains(key):
            newNode.next = self.slots[bucket]
            self.slots[bucket] = newNode

    def display(self):
        for i in range(len(self.slots)):
            current = self.slots[i]
            while current:
                print(current.key," -> ",current.value)
                current = current.next

    def contains(self, key):
        hash = self.hashCode(key)
        bucket = hash % self.size
        current = self.slots[bucket]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

hm = HashTable()

print(hm.hashCode("Nikul"))
print(hm.hashCode("Priyal"))
hm.put("Nikul",28)
hm.put("Nikel",28)
print(hm.hashCode("Priyal"))
hm.put("Priyal",27)
print(hm.hashCode(""))
hm.display()
print(hm.contains("Nikul"))
print(hm.contains("Nikel"))
