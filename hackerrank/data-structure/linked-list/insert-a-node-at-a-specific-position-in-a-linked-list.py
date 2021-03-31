#Insert a node at a specific position in a linked list https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem

def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data)
    tmpPosition = 1
    if head == None:
        head = node
    else:
        temp = head
        while temp.next != None:

            if tmpPosition == position:
                node.next = temp.next
                temp.next = node
            temp = temp.next

            tmpPosition += 1

        if tmpPosition == position:
            temp.next = node

    return head     
