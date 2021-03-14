# Source found at https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

class Node:
    """
    A node class for A* Pathfinding
    """

    def __init__(self, parent=None, position= None):
        self.parent = parent
        self.position = position

        self.G = 0  # G is the distance between the current node and the start node.
        self.H = 0  # H is the heuristic — estimated distance from the current node to the end node.
        self.F = 0  # F is the total cost of the node.

    def __eq__(self, other): 
        return self.position == other.position

    def __repr__(self):
        return f"{self.position} - G: {self.G} H: {self.H} F: {self.F}"        


    def __lt__(self, other):
        return self.F < other.F    

    def __gt__(self, other):
      return self.F > other.F     