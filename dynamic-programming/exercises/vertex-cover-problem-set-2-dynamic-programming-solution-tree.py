# Vertex Cover Problem | Set 2 https://www.geeksforgeeks.org/vertex-cover-problem-set-2-dynamic-programming-solution-tree/

class Node:
     
    def __init__(self, x):
         
        self.data = x
        self.left = None
        self.right = None

def vCover(root):
    if (root == None):
        return 0
         
    if (root.left == None and
       root.right == None):
        return 0

    size_incl = (1 + vCover(root.left) +
                     vCover(root.right))

    size_excl = 0
    if (root.left):
      size_excl += (1 + vCover(root.left.left) +
                        vCover(root.left.right)) 

    size_excl = 0
    if (root.left):
      size_excl += (1 + vCover(root.left.left) +
                        vCover(root.left.right))
    if (root.right):
      size_excl += (1 + vCover(root.right.left) +
                        vCover(root.right.right))
 
    # Return the minimum of two sizes
    return min(size_incl, size_excl)

if __name__ == '__main__':
     
    # Let us construct the tree
    # given in the above diagram
    root  = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right  = Node(22)
    root.right.right = Node(25)
 
    print("Size of the smallest vertex cover is", vCover(root))

