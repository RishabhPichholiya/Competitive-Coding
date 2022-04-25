import collections
from collections import Counter
n=int(input())
x=[]
i=0
while(n):
    n-=1 
    a,b=map(str,input().split())
    x.append([a,b])
n=len(x)
parent=[0]*n
rank=[0]*n
for i in range(n):
    parent[i]=i 
    rank[i]=0
def findPar(node):
    if(node==parent[node]):
        return node 
    parent[node]=findPar(parent[node])
    return findPar(parent[node])
def union(u,v):
    u=findPar(u) 
    v=findPar(v) 
    if(rank[u]<rank[v]):
        parent[u]=v
    elif(rank[v]<rank[u]):
        parent[v]=u 
    else:
        parent[v]=u 
        rank[u]+=1 
for i in range(n-1):
    for j in range(i+1,n):
        if(x[i][0]==x[j][0]):
            union(i,j)
        if(x[i][1]==x[j][1]):
            union(i,j) 
for i in range(n):
    parent[i]=findPar(i)
x1=Counter(parent).keys()
print(len(x1)-1)
    