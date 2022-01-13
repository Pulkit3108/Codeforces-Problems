for _ in range(int(input())):
    a,b,c=map(int,input().split())
    a1=b-(c-b)
    if(a1>=a and a1%a==0 and a1!=0):
        print('YES')
        continue
    b1=a+(c-a)//2;
    if(b1>=b and (c-a)%2==0 and b1%b==0 and b1!=0):
        print('YES')
        continue
    c1=a+2*(b-a)
    if(c1>=c and c1%c==0 and c1!=0):
        print('YES')
        continue
    print('NO')
    
