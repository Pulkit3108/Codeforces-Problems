for _ in range(int(input())):
    n=int(input())
    r1=list(input())
    r2=list(input())
    p=0
    t=[0]*n
    for i in range(n):
        if(r2[i]=='1' and r1[i]=='0'):
            p+=1
            t[i]=1
        elif(i-1>-1 and r2[i]=='1' and r1[i-1]=='1' and t[i-1]==0):
            p+=1
            t[i-1]=1
        elif(i+1<n and r2[i]=='1' and r1[i+1]=='1' and t[i+1]==0):
            p+=1
            t[i+1]=1
    print(p)
    
