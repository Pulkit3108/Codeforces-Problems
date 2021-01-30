t=int(input())
for _ in range(t): 
    n=int(input())
    a=list(map(int,input().split()))
    k=[0]*101
    for i in a:
        k[i]+=1
    print(max(k))
