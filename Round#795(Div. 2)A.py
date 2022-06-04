for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    e,o=0,0
    for i in a:
        if(i&1):
            o+=1
        else:
            e+=1
    print(min(o,e))
    
