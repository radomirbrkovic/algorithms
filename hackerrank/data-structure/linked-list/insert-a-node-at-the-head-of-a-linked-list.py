# Insert a node at the head of a linked list https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem

def insertNodeAtHead(llist, data):
    node = SinglyLinkedListNode(data)
    if llist != None:
        node.next = llist  
    
    return node    
