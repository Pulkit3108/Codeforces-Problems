t=int(input())
for _ in range(0,t):
    n=int(input())
    A=list()
    while(n!=0):
        r=n%10
        A.append(r)
        n=n//10
    x=A.count(0)
    print(len(A)-x)
    for i in range(0,len(A)):
        if(A[i]==0):
            continue
        else:
            print(A[i]*pow(10,i),end=' ')
    print()
