t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n):
        if(i==0):
            if(a[i]!=a[i+1] and a[i+1]==a[i+2]):
                break
        elif(i==n-1):
            if(a[n-1]!=a[n-2] and a[n-1]==a[n-2]):
                break
        elif(a[i]!=a[i-1] and a[i]!=a[i+1]):
            break
    print(i+1)
