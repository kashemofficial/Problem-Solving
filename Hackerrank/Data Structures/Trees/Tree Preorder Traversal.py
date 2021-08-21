def preOrder(node):
    print(node,end=" ")
    if node.left:
        preOrder(node.left)
    if node.right:
        preOrder(node.right)
