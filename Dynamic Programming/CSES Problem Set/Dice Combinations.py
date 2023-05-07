import sys,io,os
input = sys.stdin.readline
n=int(input())
mod=1000000007
if(n>=1 and n<7):
    print(2**(n-1))
else:
    dp=[0]*(n+1) 
    dp[0]=1 
    dp[1]=1
    for i in range(2,7):
        dp[i]=2*dp[i-1]
    for i in range(7,n+1):
        dp[i]=(dp[i-1]%mod+dp[i-2]%mod+dp[i-3]%mod+dp[i-4]%mod+dp[i-5]%mod+dp[i-6]%mod) %mod
    print(dp[n]%mod)
