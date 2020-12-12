t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s='a'*k
    n=n-k
    q=n//3
    s+='bca'*(q)
    n=n%3
    q=n//2
    s+='bc'*(q)
    n=n%2
    q=n
    s+='b'*(q)
    print(s)
