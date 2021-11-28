for _ in range(int(input())):
    n,l,r,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    c=0
    for i in a:
        if(i>k):
            break
        if(i<l or i>r):
            continue
        c+=1
        k-=i
    print(c)

