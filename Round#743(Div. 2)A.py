for _ in range(int(input())):
    n=int(input())
    t=input()
    s=0
    c=0
    for i in t:
        if(int(i)>0):
            s+=int(i)
            c+=1
    if(int(t[-1])>0):
        c-=1
    print(s+c)
                     
                     
