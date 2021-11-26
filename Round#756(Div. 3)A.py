for _ in range(int(input())):
    n=input()
    if(int(n[-1])%2==0):
        print(0)
    elif(int(n[0])%2==0):
        print(1)
    else:
        f=False
        for i in n:
            if(int(i)%2==0):
                f=True
                break
        if(f):
            print(2)
        else:
            print(-1)
     
