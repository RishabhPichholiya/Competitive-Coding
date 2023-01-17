
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split())) 
c=[] 
i=0 
j=0
while(i!=n and j!=m):
    if(a[i]<b[j]):
        c.append(a[i]) 
        i+=1 
    elif(a[i]==b[j]):
        c.append(a[i]) 
        i+=1 
    else:
        c.append(b[j])
        j+=1 
if(i==n):
    for it in range(j,m):
        c.append(b[it])
elif(j==m):
    for it in range(i,n):
        c.append(a[it]) 
print(*c)
