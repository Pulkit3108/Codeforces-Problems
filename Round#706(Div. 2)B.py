t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if(k==0):
        print(n)
    else:
        m1=max(a)
        m2=m1+1
        c=n
        a.sort()
        for i in range(n):
            if(i!=a[i]):
                m2=i
                break
        if(m2>m1):
            c+=k
        else:
            r=(m1+m2)//2
            if((m1+m2)%2!=0):
                r+=1
            if(r not in a):
                c+=1
        print(c)
        
