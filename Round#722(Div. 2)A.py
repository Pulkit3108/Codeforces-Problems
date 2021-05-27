for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[0]*101
    x=0
    for i in a:
        b[i]+=1
    for i in range(1,101):
        if(b[i]!=0):
            x=b[i]
            break
    print(len(a)-b[i])
        
