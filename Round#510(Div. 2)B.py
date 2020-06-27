import sys
A=dict()
A["A"]=sys.maxsize
A["B"]=sys.maxsize
A["C"]=sys.maxsize
A["ABC"]=sys.maxsize
A["AB"]=sys.maxsize
A["BC"]=sys.maxsize
A["AC"]=sys.maxsize
n=int(input())

for _ in range(0,n):
    i,c=input().split()
    a=''.join(map(str,sorted(c)))
    A[a]=min(int(i),A[a])
ans=min(A["A"]+A["B"]+A["C"],A["ABC"],A["AB"]+A["BC"],A["AB"]+A["AC"],A["AB"]+A["C"],A["BC"]+A["AC"],A["BC"]+A["A"],A["AC"]+A["B"])
if(ans==sys.maxsize):
    print("-1")
else:
    print(ans)

