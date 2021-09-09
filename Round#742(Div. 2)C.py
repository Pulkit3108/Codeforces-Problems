for _ in range(int(input())):
    n=int(input())
    c1=1
    c2=1
    i=0
    a=0
    b=0
    while(n):
        r=int(n%10)
        if(int(i%2)==0):
            a=(r*c1)+a
            c1*=10
        else:
            b=(r*c2)+b
            c2*=10
        n=int(n/10)
        i+=1
    print(((a+1)*(b+1))-2)
        


 
