# Tree Traversals (Inorder, Preorder and Postorder) https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

class Node:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def printInOrder(node):
    if node:
        # print left child
        printInOrder(node.left)

        #print node value
        print(node.val)

        #print right child
        printInOrder(node.right)

def printPreorder(node):
    if node:
        print(node.val)
        printPreorder(node.left)
        printPreorder(node.right)

def printPostorder(node):
    if node:
        printPostorder(node.left)
        printPostorder(node.right)
        print(node.val)

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print ("Preorder traversal of binary tree is ")
printPreorder(root)
 
print("In order traversal of binary tree is")
printInOrder(root)
 
print ("Postorder traversal of binary tree is")
printPostorder(root)    