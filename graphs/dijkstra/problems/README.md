# Dijkstra's shortest path tree algorithm - Practice

## [Problem 1](https://practice.geeksforgeeks.org/problems/shortest-path-from-1-to-n/0)

Consider a directed graph whose vertices are numbered from 1 to n. There is an edge from a vertex i to a vertex j iff either j = i + 1 or j = 3i. The task is to find the minimum number of edges in a path in G from vertex 1 to vertex n.

**Input:**

The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.

Each test case contains a value of n. 

**Output:**

Print the number of edges in the shortest path from 1 to n.

**Constraints:**

1<=T<=30

1<=n <=1000

**Example:**

    Input: 2, 9, 4
    Output: 2, 2


## Problem 2

We have input graph with six nodes (vertices) in following order `{S, A, B, C, D, T}`, where `S` is starting node and `T` is target node. The tax is find the shortest path from starting to targeting node. 

**Input**

```
graph = {
    'S': {'A': 2, 'B': 3},
    'A': {'B': 1, 'C': 5},
    'B': {'D': 7},
    'C': {'D': 2, 'T': 5},
    'D': {'T': 2},
    'T': {}
}
```

**Output**

```
11
```