def functionality(x,y):
    return min(x,y)
def build(arr,start,end,index):
    #Time Complexity O(n)
    if(start==end):
        segTree[index]=arr[start]
        return 
    mid=(start+end)//2 
    left=2*index
    right=(2*index)+1
    build(arr,start,mid,2*index)
    build(arr,mid+1,end,2*index+1)
    segTree[index]=min(segTree[left],segTree[right])
    
def update(arr,start,end,index,pos,value):
    # Time Complexity O(logn)
    if(start==end):
        arr[pos]=value 
        segTree[index]=arr[pos] 
        return 
    mid=(start+end)//2 
    if(mid>=pos):
        update(arr,start,mid,2*index,pos,value)
    else:
        update(arr,mid+1,end,2*index+1,pos,value)
    segTree[index]=min(segTree[2*index],segTree[2*index+1])
    
def query(start,end,index,l,r):
    # Time Complexity O(logn)
    if(start>=l and end<=r):
        return segTree[index] 
    if(l>end or r<start):
        return 1e9+7 
    mid=(start+end)//2 
    leftAnswer = query(start,mid, 2*index,l,r) 
    rightAnswer = query(mid+1,end, 2*index+1,l,r)
    return min(leftAnswer,rightAnswer)
    
    
n,m=map(int,input().split())
a=list(map(int,input().split()))
#if n is a power of 2
segTree=[-1e9+7]*((4*n))
build(a,0,n-1,1)
for i in range(m): 
    p,q,r=map(int,input().split()) 
    if(p==1):
        update(a,0,n-1,1,q,r) 
    else:
        print(query(0,n-1,1,q,r-1))
        
# 1+2+4+8.....n = 2*n-1 if n is a power of 2 
#[111111111]=2*(n)-1 
# if n is not a power of 2 -> convert it to  a next power of 2 
# for any given , next power of 2 for n will be <=2*n 
#Convert n to next power of 2 -> <=2n ->2*(2n)-1 <=4n 
