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
        else:
            current = self.slots[bucket]
            while current:
                if current.key == key:
                    current.value = value
                current = current.next

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

    def get(self, key):
        hash = self.hashCode(key)
        bucket = hash % self.size
        current = self.slots[bucket]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def getSize(self):
        size = 0
        for i in range(len(self.slots)):
            current = self.slots[i]
            while current:
                size += 1
                current = current.next
        return size

    def delete(self, key):
        hash = self.hashCode(key)
        bucket = hash % self.size
        # if key found at the head
        if self.slots[bucket].key == key:
            self.slots[bucket] = self.slots[bucket].next
        else:
            current = self.slots[bucket]
            while current.next:
                if current.next.key == key:
                    current.next = current.next.next
                current = current.next

    # We can access element using hm["key"]
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


hm = HashTable()

print(hm.getSize())
#print(hm.hashCode("Nikul"))
#print(hm.hashCode("Priyal"))
hm.put("Nikul",28)
hm.put("Nikul",29)
hm["Nikel"] = 30
hm.put("Priyal",27)
#print(hm.hashCode("Priyal"))
#print(hm.hashCode(""))
print("")
hm.display()
print(hm.contains("Nikul"))
print(hm.contains("Nikel"))

print(hm["Nikul"])
print(hm.get("Priyal"))
print(hm.get("Piyal"))
print(hm.getSize())
print("")
hm.delete("Nikel")
hm.display()
