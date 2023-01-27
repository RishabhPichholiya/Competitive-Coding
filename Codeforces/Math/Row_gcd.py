import math
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a1=a.copy()
a1.sort()
if(n==1):
    ans=[]
    for i in range(m):
        ans.append((a[0]+b[i]))
    print(*ans)
else:
    x=a[1]-a[0]
    for i in range(1,n):
        x=math.gcd(x,a[i]-a[0]) 
    ans=[]
    for i in range(m):
        ans.append(math.gcd((a[0]+b[i]),x))
    print(*ans)
    
