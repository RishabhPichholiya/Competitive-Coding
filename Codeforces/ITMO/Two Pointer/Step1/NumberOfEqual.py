from collections import Counter 
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
key1=list(Counter(a).keys())
val1=list(Counter(a).values())
key2=list(Counter(b).keys())
val2=list(Counter(b).values())
i=0 
j=0 
ans=0
while(i!=len(key1) and j!=len(key2)):
    if(key1[i]==key2[j]):
        ans+=val1[i]*val2[j]
        i+=1 
        j+=1 
    elif(key1[i]>key2[j]):
        j+=1 
    else:
        i+=1 
print(ans)   
