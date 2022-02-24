for _ in range(int(input())):
    x=list()
    y=list()
    for i in range(3):
        a,b=map(int,input().split())
        x.append(a)
        y.append(b)
    if((y[0]==y[1] and y[2]<y[1]) or (y[1]==y[2] and y[0]<y[1]) or (y[2]==y[0] and y[1]<y[2])):
        if(y[0]==y[1]):
            print(abs(x[0]-x[1]))
        elif(y[1]==y[2]):
            print(abs(x[1]-x[2]))
        else:
            print(abs(x[2]-x[0]))
    else:
        print(0)
        
    



        
