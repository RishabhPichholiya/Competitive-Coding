import sys,io,os
input = sys.stdin.readline
n,x=map(int,input().split())
a=list(map(int,input().split()))
dp=[0]*(x+1) 
for i in range(1,x+1):
    y=int(1e9)
    for j in range(n):
        if(i-a[j]>=0):
            y=min(y,dp[i-a[j]]) 
    dp[i]=1+ y 
if(dp[x]==int(1e9)+1):
    print(-1)
else:
    print(dp[x])
