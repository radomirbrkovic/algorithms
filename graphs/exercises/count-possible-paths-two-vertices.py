# Count all possible paths between two vertices https://www.geeksforgeeks.org/count-possible-paths-two-vertices/

class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def addEdge(self, u, v):
        self.adj[u].append(v)

    def countPathUtil(self, u, d, visited, count):
        visited[u] = True

        if u == d:
            count[0] += 1
        else:
            i = 0
            while i < len(self.adj[u]):
                if not visited[self.adj[u][i]]:
                    self.countPathUtil(self.adj[u][i], d, visited, count)
                i+=1    

        visited[u] = False


    def countPaths(self, s, d):
        visited = [False] * self.V
        count = [0]
        self.countPathUtil(s, d, visited, count)    
        return count[0]

if __name__ == '__main__':
 
    # Create a graph given in the
    # above diagram
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)
 
    s = 2
    d = 3
    print(g.countPaths(s, d))