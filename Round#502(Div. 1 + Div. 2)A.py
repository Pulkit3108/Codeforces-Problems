n=int(input())
A=list()
for i in range(n):
    a,b,c,d=map(int,input().split())
    A.append(a+b+c+d)
k=A[0]
A.sort(reverse=True)
print(A.index(k)+1)
