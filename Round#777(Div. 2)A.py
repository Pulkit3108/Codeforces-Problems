for _ in range(int(input())):
    n=int(input())
    t=0
    if(n%3==1):
        t=1;
    else:
        t=2;
    s=0;
    while(s!=n):
        print(t,end='')
        s+=t
        t=3-t
    print()



        
