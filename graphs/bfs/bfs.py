# Program for print BFS traversal from
# a given source vertex. BFS(int s)
# traverses vertices reachable from s

from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation

class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print BFS of graph
    def BFS(self, s):

        # Mark all the vertives as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print s, ", \t"  

            # Get all adjacent vertices of the dequeued vertex s. 
            # If a adjacent has not been visited, than mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


# Run code 

# Create a graph {2, 0, 3, 1} 

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.BFS(2)



