def pow(a,b):
    c=1 
    while(b):
        if(b%2!=0):
            c*=a 
            
        a*=a
        a=a%(int((1e9)+7))
        b=b//2 
    return c%(int((1e9)+7))
n=int(input())
while(n):
    n-=1 
    a,b,c=map(int,input().split()) 
    if(a==0 and b==0):
        print(1) 
    elif(b==0 and c==0):
        print(a) 
    elif(a==0 and c==0):
        print(0) 
    else:
        x=pow(b,c)
        x=int(x)
        x=pow(a,x)
        print(int(x))