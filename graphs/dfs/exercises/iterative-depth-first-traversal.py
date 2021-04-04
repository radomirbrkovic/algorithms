# Iterative Depth First Traversal of Graph https://www.geeksforgeeks.org/iterative-depth-first-traversal/

class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = [[] for i in range(V)]

    def addEdge(self, v, w):
        self.graph[v].append(w)

    def DFS(self, s):

        visited = [False for i in range(self.V)]
        stack= []
        stack.append(s)

        while(len(stack)):
             # Pop a vertex from stack and print it
            s = stack[-1]
            stack.pop()

            if s not in visited:
                visited[s] = True
                print(s, end=' ')

            for node in self.graph[s]:
                if node not in visited:
                    stack.append(node)


if __name__=="__main__":
    g = Graph(5); # Total 5 vertices in graph
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(0, 3)
    g.addEdge(1, 4)
 
    print("Following is Depth First Traversal")
    g.DFS(0)                         
