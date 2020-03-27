# [Breadth first search or BFS for Graphs](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/) 

[Breadth First Traversal (or Search)](https://en.wikipedia.org/wiki/Breadth-first_search) for graph is similar to [Level Order Tree Traversal](https://www.geeksforgeeks.org/level-order-tree-traversal/). The only catch here is, unlike trees, graphs may contain cycles, so we may come to same node again. To avoid processing node more than once, we use a boolean visited array. For simplicity, it is assumed that all verticals are reachable from starting vertex. 

For example, in the following graph, we started traversal from vertex 2. When we come to vertex 0, we look for all adjacent vertices of it. 2 is also an adjacent vertex of 0. If we don't mark visited vertices, then 2 will be processed again and it will become a non-terminating process. 

A representation of Breadth First Search for graph `{2, 0, 3, 1}`  is on the following image 

![Full graph](https://media.geeksforgeeks.org/wp-content/uploads/bfs-5.png "Full graph")