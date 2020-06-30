t=int(input())
for _ in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    e=0
    o=0
    for i in A:
        if(i%2==0):
            e+=1
        else:
            o+=1
    if(o==0 or e==0):
        print("YES")
    else:
        print("NO") 
    


