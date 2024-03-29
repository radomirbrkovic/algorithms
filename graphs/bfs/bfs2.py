Graph = {
    "John": {"Steve", "Mike", "Bob"},
    "Steve": {"Jim", "John"},
    "Mike": {"Luke", "John"},
    "Bob": {"John"},
    "Jim": {"Steve"},
    "Luke": {"Mike"}
}

def bfs(graph, start):
    visited = []
    queue =[start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                   queue.append(neighbor)
    return visited

print(bfs(Graph, "John"))                    