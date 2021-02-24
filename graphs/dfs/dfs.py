Graph = {
    "John": {"Steve", "Mike", "Bob"},
    "Steve": {"Jim", "John"},
    "Mike": {"Luke", "John"},
    "Bob": {"John"},
    "Jim": {"Steve"},
    "Luke": {"Mike"}
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)

    return visited

print(dfs(Graph, 'John'))            