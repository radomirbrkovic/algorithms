# Graph representation using set and hash | [Source](https://www.geeksforgeeks.org/graph-representations-using-set-hash/)


A set is different from a vector in tow ways: it stories elements in a sorted way, and duplicated elements are not allowed. Therefore, this approach can't be used for graphs containing parallel edges. Since sets are internally implemented as binary search trees, an edge between two vertices can be searched in O(logV) time, where V is the number of vertices in the graph. Sets in python are unordered and not indexed. Hence, for python we will be using dictionary which will have source vertex key and its adjacency list will be sorted and a set format as value for that kay. 
