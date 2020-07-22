t=int(input())
for _ in range(0,t):
    n,m=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    a=9999
    for i in A:
        for j in B:
            if(i==j):
                a=i
                break
    if(a==9999):
        print("No")
    else:
        print("Yes")
        print(1,a)




    
