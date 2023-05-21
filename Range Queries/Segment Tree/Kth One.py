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
    segTree[index]=segTree[left]+segTree[right]
    
def update(arr,start,end,index,pos):
    # Time Complexity O(logn)
    if(start==end):
        arr[pos]=1-arr[pos]
        segTree[index]=arr[pos] 
        return 
    mid=(start+end)//2 
    if(mid>=pos):
        update(arr,start,mid,2*index,pos)
    else:
        update(arr,mid+1,end,2*index+1,pos)
    segTree[index]=segTree[2*index]+segTree[2*index+1]
    
def search(start,end,index,val):
    # Time Complexity O(logn)
    if(start==end):
        return start
    mid=(start+end)//2
    if(segTree[2*index]>=val):
        return search(start, mid,2*index,val) 
    if(val-segTree[2*index]>0):
        return search(mid+1, end,2*index+1,val-segTree[2*index])
    
n,m=map(int,input().split())
a=list(map(int,input().split()))
#if n is a power of 2
segTree=[0]*((4*n))
build(a,0,n-1,1)
for i in range(m): 
    p,q=map(int,input().split()) 
    if(p==1):
        update(a,0,n-1,1,q) 
    else:
        print(search(0,n-1,1,q+1))
# 1+2+4+8.....n = 2*n-1 if n is a power of 2 
#[111111111]=2*(n)-1 
# if n is not a power of 2 -> convert it to  a next power of 2 
# for any given , next power of 2 for n will be <=2*n 
#Convert n to next power of 2 -> <=2n ->2*(2n)-1 <=4n 
