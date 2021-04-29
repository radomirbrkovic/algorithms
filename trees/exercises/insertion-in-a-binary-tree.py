# Insertion in a Binary Tree in level order https://www.geeksforgeeks.org/insertion-in-a-binary-tree-in-level-order/

class Node():
    
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

""" Inorder traversal of a binary tree"""
def traveres(node):

    if not node:
        return

    traveres(node.left)
    print(node.val, end=" ")
    traveres(node.right)

# insert node in right place in the binary tree
def insert(node, value):

    # make root node    
    if not node:
        root = Node(value)
        return

    q = []
    q.append(node)

    while (len(q)):

        node = q[0]
        q.pop(0)

        if not node.left:
            node.left = Node(value)
            break
        else:
            q.append(node.left)

        if not node.right:
            node.right = Node(value)
            break
        else:
            q.append(node.right) 

# Driver code
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
 
    print("Inorder traversal before insertion:", end = " ")
    traveres(root)
 
    key = 12
    insert(root, key)
 
    print()
    print("Inorder traversal after insertion:", end = " ")
    traveres(root)                   

