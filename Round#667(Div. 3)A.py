t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    c=abs(b-a)
    x=c%10
    a=c//10
    if(x!=0):
        a+=1
    print(a)
