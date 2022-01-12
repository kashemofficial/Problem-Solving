def reversePrint(llist):
    # Write your code here
    if llist:
        reversePrint(llist.next)
        print(llist.data)