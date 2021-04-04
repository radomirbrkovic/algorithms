# program to find a mother vertex in O(V+E) time
from collections import defaultdict

# This class represents a directed graph using adjacency list representation
class Graph(object):
    def __init__(self, vertices):
        self.V = vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary

    def addEdge(self, v, w):
        self.graph[v].append(w)

    def DFSUtil(self, v, visited):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)      

    # Returns a mother vertex if exists. Otherwise returns -1
    def findMother(self):
        # visited[] is used for DFS. Initially all are initialized as not visited
        visited = [False] * (self.V)
        # To store last finished vertex (or mother vertex)
        v=0
 
        for i in range(self.V):
            if visited[i] == False:
                self.DFSUtil(i, visited)
                v = i

        visited = [False] * (self.V)
        self.DFSUtil(v, visited)
        if any(i == False for i in visited):
            return -1
        else:
            return v    


# Driver code
if __name__=="__main__":
    g = Graph(7)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(4, 1)
    g.addEdge(6, 4)
    g.addEdge(5, 6)
    g.addEdge(5, 2)
    g.addEdge(6, 0)
    print("A mother vertex is " + str(g.findMother()))