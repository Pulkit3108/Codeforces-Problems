n=int(input())
A=list(map(int,input().split()))
A.sort()
if(n<3):
    print(0)
else:
    a=A[n-2]-A[0]
    b=A[n-1]-A[1]
    print(min(a,b))


