for _ in range(int(input())):
    a,b=map(int,input().split())
    x=0
    if((a-1)%4==0):
        x=a-1
    elif((a-1)%4==1):
        x=1
    elif((a-1)%4==2):
        x=a

    if(x==b):
        print(a)
    else:
        if(x^b==a):
            print(a+2)
        else:
            print(a+1)
