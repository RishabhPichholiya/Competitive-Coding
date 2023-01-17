n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split())) 
c=[] 
i=0
j=0 
ct=0
while(i!=n and j!=m):
    if(a[i]<b[j]):
        ct+=1  
        i+=1 
        
    else:
        c.append(ct) 
        j+=1 
if(len(c)!=m):
    arr=[n]*(m-len(c)) 
    c.extend(arr) 
print(*c)
