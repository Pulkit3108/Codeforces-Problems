for _ in range(int(input())):
    n=int(input())
    p=list(map(int,input().split()))
    s=0
    i=1
    while(i<n):
        if(p[i-1]>p[i]):
            i+=2
            s+=1
        else:
            i+=1
    print(s)
