n,k=map(int,input().split())
A=set(map(int,input().split()))
A.add(0)
c=0
c1=0
A=list(A)
A.sort()
while(c1<k):
    if(c==len(A)-1):
        print(0)
    else:
        print(A[c+1]-A[c])
        c+=1
    c1+=1
