for _ in range(int(input())):
    n=int(input())
    s=input()
    t=""
    for i in s:
        if(i=='U'):
            t+='D'
        elif(i=='D'):
            t+='U'
        else:
            t+=i
    print(t)
            
