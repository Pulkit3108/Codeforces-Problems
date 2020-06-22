t= int(input())
for _ in range(0,t):
    n,k=map(int,input().split())
    A=['a']*n
    for i in range(n-2,-1,-1):
        if(k<=n-i-1):
            A[i]='b'
            A[n-k]='b'
            break
        k-=n-i-1
    print(''.join(map(str,A)))



    
