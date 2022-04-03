for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    if(n>1):
        if(a[-1]-a[-2]>1):
            print("NO")
        else:
            print("YES")
    else:
        if(a[0]>1):
            print("NO")
        else:
            print("YES")
    
