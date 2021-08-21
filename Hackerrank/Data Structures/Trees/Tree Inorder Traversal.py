def inOrder(root):
    #Write your code here
    if root.left:
        inOrder(root.left)
    print(root,end=" ")
    if root.right:
        inOrder(root.right)