n=int(input())
A=list(map(int,input().split()))
c=0
mi=min(A)
ma=max(A)
a=ma-mi+1
print(a-n)
