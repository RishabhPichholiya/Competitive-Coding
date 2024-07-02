def inorder(root):
    ans=[]
    cur=root
    while cur is not None:
        if(cur.left==None):
            ans.append(cur.val)
            cur=cur.right 
        else:
            temp=cur.left
            while(temp.right and temp.right!=cur):
                temp=temp.right
            if(temp.right==None):
                temp.right=cur
                cur=cur.left
            else:
                temp.right=None
                ans.append(cur.val) 
                cur=cur.right
        return ans
    
def preorder(root):
    ans=[]
    cur =root 
    while cur is not None: 
        if(cur.left==None):
            ans.append(cur.val)
            cur=cur.right 
        else:
            prev=cur.left
            while(prev.right and prev.right!=cur):
                prev=prev.right 
            if(prev.right==None):
                prev.right=cur 
                ans.append(cur.val)
                cur=cur.left
            else:
                prev.right=None 
                cur=cur.right
    return ans


