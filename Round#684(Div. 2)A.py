t=int(input())
for _ in range(t):
    n,c0,c1,h=map(int,input().split())
    s=input()
    a=s.count('0')
    b=s.count('1')
    c=c0*a+c1*b
    if(c0+h<c1):
        c=c0*a+(c0+h)*b
    elif(c1+h<c0):
        c=(c1+h)*a+c1*b
    print(c)
        
        
