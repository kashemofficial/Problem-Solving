def insertNodeAtTail(head,data):
    if head is None:
        return SinglyLinkedListNode(data)
    pnt = head
    while pnt.next:
        pnt = pnt.next
    pnt.next = SinglyLinkedListNode(data)
    return head

"""class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def print_singly_linked_list(self):
    temp = self.head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next

def insertNodeAtHead(llist, data):
    x = SinglyLinkedListNode(data)
    if (llist == None):
        llist = x
    else:
        new_node = x
        new_node.next = llist
        llist = new_node
    return llist

if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()
    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
    print_singly_linked_list(llist)"""

