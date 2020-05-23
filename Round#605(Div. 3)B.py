T=int(input())
for _ in range(0,T):
    A=list()
    s=input()
    u=0
    d=0
    l=0
    r=0
    for i in s:
        if(i=='U'):
            u+=1
        elif(i=='D'):
            d+=1
        elif(i=='L'):
            l+=1
        else:
            r+=1
    u=d=min(u,d)
    l=r=min(l,r)
    S=''
    if(u and d and l and r):
        while(u!=0):
            u-=1
            S+='U'
        while(r!=0):
            r-=1
            S+='R'
        while(d!=0):
            d-=1
            S+='D'
        while(l!=0):
            l-=1
            S+='L'
        
    else:
        if(r and l):
            S+="LR"
        elif(u and d):
            S+="UD"
    print(len(S))
    print(S)

