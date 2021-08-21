def insertNodeAtTail(head,data):
    if head is None:
        return SinglyLinkedListNode(data)
    pnt = head
    while pnt.next:
        pnt = pnt.next
    pnt.next = SinglyLinkedListNode(data)
    return head

