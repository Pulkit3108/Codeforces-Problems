A=list(map(int,input().split()))
A.sort()
if((A[3])==(A[0]+A[1]+A[2]) or (A[3]+A[0])==(A[1]+A[2])):
    print("YES")
else:
    print("NO")
