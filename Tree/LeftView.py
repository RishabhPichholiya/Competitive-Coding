# Recursive DFS Solution
def leftView(root):
    leftview = [] 
    left(root,0,leftview)
    return leftview

def left(root, level, arr):
    if(root):
        if(level==len(arr)):
            arr.append(root.val)
        left(root.left, level+1, arr)
        left(root.right, level+1, arr)
        
# Iterative Level Order traversal 

def leftViewTraversal(root):
    q=[]
    q.append(root)
    q.append(None)
    temp=[]
    ans=[]
    while(q):
        x=q.pop(0)
        temp.append(x)
        if(x==None):
            ans=[temp[0]]
            temp=[]
            if(len(q)>0):
                q.append(None)
        else:
            if(x.left):
                q.append(x.left)
            if(x.right):
                q.append(x.right)
    return ans