n,k=map(int,input().split()) 
import math
def primeFactors(n,arr):
	while(n%2==0):
		arr.append(2)
		n = n / 2
	for i in range(3,int(math.sqrt(n))+1,2):
		while(n%i==0):
			arr.append(i),
			n = n / i
	if n > 2:
		arr.append(n)
arr=[]
primeFactors(n,arr)
ans=[]
if(len(arr)>=k):
    x=1
    for i in range(k-1):
        x*=arr[i]
        ans.append(arr[i]) 
    x1=n//x 
    if(x1==1):
        print(-1) 
    else:
        ans.append(x1) 
        print(*ans)
else:
    print(-1)
