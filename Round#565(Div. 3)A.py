q=int(input())
for _ in range(q):
    n=int(input())
    c1=0
    c2=0
    c3=0
    while(n%2==0):
        n=n//2
        c1+=1
    while(n%3==0):
        n=n//3
        c2+=1
    while(n%5==0):
        n=n//5
        c3+=1
    if(n==1):
        print(c1+2*c2+3*c3)
    else:
        print(-1)