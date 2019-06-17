from Vertex import *

class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def addEdge(self, v1, v2, cost=0):
        if v1 not in self.vertList:
            self.addVertex(v1)
        if v2 not in self.vertList:
            self.addVertex(v2)
        self.vertList[v1].addNeighbour(self.vertList[v2], cost)

    def getVertex(self, v):
        if v not in self.vertList:
            return None
        return self.vertList[v]

    def getVertices(self):
        return self.vertList.keys()

    def __contains__(self, v):
        return (v in self.vertList)

    def __iter__(self):
        return iter(self.vertList.values())

g = Graph()
for i in range(6):
    g.addVertex(i)

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)


for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))
