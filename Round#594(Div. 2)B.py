n=int(input())
A=list(map(int,input().split()))
A.sort()
c1=sum(A[:n//2])
c2=sum(A)-c1
print((c1**2)+(c2**2))
