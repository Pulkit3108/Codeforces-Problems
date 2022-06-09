for _ in range(int(input())):
    n=int(input())
    f,s,t=0,0,0
    for _ in range(n):
        if(s-t>1):
            t+=1
        elif(f-s>1):
            s+=1
        else:
            f+=1
    print(s,f,t)
