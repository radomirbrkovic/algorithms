# Insert a Node at the Tail of a Linked List https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem

def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)

    if head == None:
        head = node
    else:
        temp = head
        while temp.next != None:
            temp = temp.next

        temp.next = node

    return head        
