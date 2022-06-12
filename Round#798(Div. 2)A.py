for _ in range(int(input())):
    n,m,k=map(int,input().split())
    a=sorted(input())
    b=sorted(input())
    c=list()
    op1,op2=k,k
    i,j=0,0
    while(i<len(a) and j<len(b)):
        if((a[i]<=b[j] and op1>0) or op2<=0):
            c.append(a[i])
            op1-=1
            op2=k
            i+=1
        else:
            c.append(b[j])
            op2-=1
            op1=k
            j+=1
    print(''.join(map(str,c)))
