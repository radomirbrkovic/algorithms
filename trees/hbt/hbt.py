# For implementing binary tree we need two classes
# Node class that will represent tree node 
# BinaryTree class  that represent structure of binary tree
# with all necessary functions 


class Node:
    
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, root):
        self.root = Node(root)

    def getHeight(self, node):
        
        if node is None:
            return -1
        
        leftHight = self.getHeight(node.left)
        rightHight = self.getHeight(node.right)

        return 1 + max(leftHight, rightHight)


# executing code 

tree = BinaryTree(3)
tree.root.left = Node(2)
tree.root.right = Node(5)

tree.root.left.left = Node(1)

tree.root.right.left = Node(4)
tree.root.right.right = Node(6)

tree.root.right.right.left = Node(7)

print tree.getHeight(tree.root)
