import collections
class Graph:

    def __init__(self, startingNode, targetNode):
        # default dictionary to store graph
        self.graph = collections.defaultdict(list)
        self.start = startingNode
        self.target = targetNode
        self.distances = {startingNode: 0}
        self.path = {}
        self.minPath = [];

    def addDistance(self, node, target = None, distance = 0):
        if target != None:
            self.graph[node].append({target: distance})
        else:
            self.graph[node].append({})   

    def minDistances(self, node, dist):

     
        # calculating min distances between nodes         
        for item in dist:
            key=item.keys()[0]
            distance = item.values()[0]
            parentDistance = self.distances.get(node)
            
            if self.distances.get(key) == None or self.distances.get(key) > distance + parentDistance:
                self.distances[key] = distance + parentDistance 
                self.path[key] = node

    def getMinPath(self, node):
        

        if self.path.get(node):
            self.minPath.append(self.path.get(node))

        if node != self.start:
            self.getMinPath(self.path.get(node))    

            
    def dijkstra(self):

        self.graph = collections.OrderedDict(sorted(self.graph.items())) 
        for node in self.graph.keys():
           if self.graph[node] != None and node != self.target:
               self.minDistances(node, self.graph[node])

        self.minPath.append(self.target)
        self.getMinPath(self.target)
        self.minPath.sort()

        print self.minPath
        print self.distances[self.target]


# Execute code 

graph = Graph('0', '5')

graph.addDistance('0', '1', 2)
graph.addDistance('0', '2', 3)
graph.addDistance('1', '2', 1)
graph.addDistance('1', '3', 5)
graph.addDistance('2', '4', 7)
graph.addDistance('3', '5', 5)
graph.addDistance('3', '4', 2)
graph.addDistance('4', '5', 4)
graph.addDistance('5')

graph.dijkstra()
