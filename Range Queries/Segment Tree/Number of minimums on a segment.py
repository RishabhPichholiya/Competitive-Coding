import io,os,sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def build(arr,start,end,index):
    #Time Complexity O(n)
    if(start==end):
        segTree[index][0]=arr[start]
        segTree[index][1]=1
        return 
    mid=(start+end)//2 
    left=2*index
    right=(2*index)+1
    build(arr,start,mid,2*index)
    build(arr,mid+1,end,2*index+1)
    segTree[index][0]=min(segTree[left][0],segTree[right][0])
    if(segTree[left][0]<segTree[right][0]):
        segTree[index][1]=segTree[left][1]
    elif(segTree[left][0]>segTree[right][0]):
        segTree[index][1]=segTree[right][1]
    else:
        segTree[index][1]=segTree[left][1]+segTree[right][1]
    
def update(arr,start,end,index,pos,value):
    # Time Complexity O(logn)
    if(start==end):
        arr[pos]=value 
        segTree[index][0]=arr[pos]
        segTree[index][1]=1
        return 
    mid=(start+end)//2 
    if(mid>=pos):
        update(arr,start,mid,2*index,pos,value)
    else:
        update(arr,mid+1,end,2*index+1,pos,value)
    segTree[index][0]=min(segTree[2*index][0],segTree[2*index+1][0])
    if(segTree[2*index][0]<segTree[2*index+1][0]):
        segTree[index][1]=segTree[2*index][1] 
    elif(segTree[2*index][0]==segTree[2*index+1][0]):
        segTree[index][1]=segTree[2*index][1]+segTree[2*index+1][1] 
    else:
        segTree[index][1]=segTree[2*index+1][1] 
        
def query(start,end,index,l,r):
    # Time Complexity O(logn)
    if(start>=l and end<=r):
        return segTree[index]
    if(l>end or r<start):
        return [int(1e9+7),0] 
    mid=(start+end)//2 
    leftAnswer = query(start,mid, 2*index,l,r)
    rightAnswer = query(mid+1,end, 2*index+1,l,r)
    if(leftAnswer[0]<rightAnswer[0]):
        return leftAnswer
    elif(leftAnswer[0]==rightAnswer[0]):
        return [leftAnswer[0],leftAnswer[1]+rightAnswer[1]]
    else:
        return rightAnswer
    
n,m=map(int,input().split())
a=list(map(int,input().split()))
#if n is a power of 2
segTree=[]
for i in range(4*n):
    segTree.append([int(1e9+7),0])
build(a,0,n-1,1)
for i in range(m): 
    p,q,r=map(int,input().split()) 
    if(p==1):
        update(a,0,n-1,1,q,r) 
    else:
        sys.stdout.write(" ".join(map(str,query(0,n-1,1,q,r-1))) + "\n")
