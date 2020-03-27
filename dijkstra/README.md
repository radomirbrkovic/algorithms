# [Dijkstra's shortest path algorithm](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/) 

Given a graph and a source vertex in the graph, find shortest paths from source to all vertices and given graph. 

Dijkstra's algorithm is very similar to [Prims's algorithm for minimum spanning tree](https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/). Like Prime's MST, we generate a SPT (shortest path tree) with given source as root. We maintain two sets, one set contains verticals included in shortest path tree, other set set includes verticals not yet included in shortest path tree. At every step of algorithm, we find a vertex which is in the other set (set of not yet included) and has a minimum distance from the source. 

Below are detailed steps of used in Dijkstra's algorithm to find the shortest path from a single source vertex to all other vertices in the given graph. 

### Algorithm steps

1. Create a set `sptSet`(shortest path tree set) that keeps track of vertices included in shortest path tree, i.e. whose minimum distance from source is calculated and finalized. Initially , this set is empty. 
2. Assign a distance value to all vertices in the input graph. Initialize all distance values as **INFINITE**. Assign distance value as 0 for the source vertex so that is picked first. 
3. When `sptSet` doesn't include all vertices:
    - Pick a vertex `u` which is not there in `sptSet` and has minimum distance value.
    - Include `u` in `sptSet`
    - Update distance value of all adjacent vertices of `u`. To update the distance values, iterate through all adjacent vertices. For every adjacent vertex `v`, if sum of distance value of `u` (from source) and weight of edge `u-v`, is less than the distance value of `v`, then update the distance value of `v`.    

### Example

As example we have the following given graph:
![Full graph](https://www.geeksforgeeks.org/wp-content/uploads/Fig-11.jpg "Full graph")

The set `sptSet` is initially empty and distances assigned to vertices are `{0, INF, INF, INF, INF, INF, INF, INF}` where `INF` indicates infinity. Now pick the vertex with minimum distance value. The vertex 0 is picked, include it in `sptSet`, so `sptSet` become `{0}`. After including 0 to `sptSet`, update distance value of its adjacent vertices. Adjacent vertices of 0 are 1 and 7. The distance values of 1 and 7 are updated as 4 and 8. Following subgraph shows vertices and their distance value, only the vertices with finite distance values are shown. The vertices include in SPT are show in green color.

![](https://www.geeksforgeeks.org/wp-content/uploads/MST1.jpg "")

Pick the vertex with minimum distance value and not already included in SPT (not in `sptSet`). The vertex 1 is picked and added to `sptSet`, so `sptSet` now becomes `{0, 1}`. Update the distance values of adjacent vertices of 1. The distance value of vertex 2 becomes 12. 

![](https://www.geeksforgeeks.org/wp-content/uploads/DIJ2.jpg "")  

Pick the vertex with minimum distance value and not already included in SPT (not in `sptSet`). Our minimum distance is 8 so next vertex which be picked is 7, so `sptSet` now becomes `{0, 1 7}`. Now update the distance values of adjacent vertices of 7 which are not included in SPT. The distance value of  vertex 6 and 8 becomes finite (15 and 9 respectively)

![](https://www.geeksforgeeks.org/wp-content/uploads/DIJ3.jpg "")  

Pick the vertex with minimum distance value and not already included in SPT (not in `sptSet`). Vertex 6 is picked, so `sptSet` now becomes `{0, 1, 7 , 6}`. Update the distance values of adjacent vertices of 6. The distance value of vertex 5 and 8 are update (11 and 15 respectively)

![](https://www.geeksforgeeks.org/wp-content/uploads/DIJ4.jpg "")

We repeat the above steps until `sptSet` does include all vertices of given graph. Finally, we get yhe following Shortest path tree (SPT)

![](https://www.geeksforgeeks.org/wp-content/uploads/DIJ5.jpg "")
