import sys
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    m=0
    k=sys.maxsize
    if(b==1):
        b+=1
        m+=1
    for i in range(10):
        m1=m+i
        b1=b+i
        a1=a
        while(a1!=0):
            a1=a1//b1
            m1+=1
        k=min(k,m1)
    print(k)
