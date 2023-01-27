n,m=map(int,input().split())
ans=4*(2**(n-1))*(2**(m-1))
print(ans%998244353)
