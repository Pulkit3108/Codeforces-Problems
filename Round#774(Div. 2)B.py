for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    k=(n-1)//2
    s1=s2=0
    for i in range(n-1,n-k-1,-1):
        s1+=a[i]
    for i in range(k+1):
        s2+=a[i]
    if(s1>s2):
        print("YES")
    else:
        print("NO")
    
    



        
