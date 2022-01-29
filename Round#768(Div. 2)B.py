for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=a[::-1]
    m=0
    p=1;
    while(p<n):
        if(b[p]==b[0]):
            p+=1
            continue;
        m+=1;
        p*=2;
    print(m)
