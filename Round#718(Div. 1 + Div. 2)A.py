for _ in range(int(input())):
    n=int(input())
    if(n>=2050 and n%2050==0):
        k=n//2050
        s=0
        while(k!=0):
            r=k%10
            k=k//10
            s+=r
        print(s)
    else:
        print(-1)
