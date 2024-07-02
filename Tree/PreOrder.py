def preOrder(root):
    if(root):
        print(root.val)
        preOrder(root.left)
        preOrder(root.right)
        

    