def inorder(root):
    if(root):
        inorder(root.left)
        print(root.val)
        inorder(root.right) 

def postorder(root):
    if(root):
        postorder(root.left)
        postorder(root.right)
        print(root.val)