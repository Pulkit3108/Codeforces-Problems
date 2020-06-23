t= int(input())
for _ in range(0,t):
    n=int(input())
    A=list(map(int,input().split()))
    e=0
    o=0
    for i in range(0,n):
        if(A[i]%2==0):
            e+=1
        else:
            o+=1
    if(n%2==0):
        if(e==0 or o==0):
            print("NO")
        else:
            print("YES")
    else:
        if(o==0):
            print("NO")
        else:
            print("YES")


        




    
