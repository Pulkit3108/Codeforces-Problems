t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=list(input())
    a=0
    for i in range(n):
        if(s[i]=='*'):
            s[i]='x'
            t1=i
            a+=1
            break
    for i in range(n-1,-1,-1):
        if(s[i]=='*'):
            s[i]='x'
            t2=i
            a+=1
            break
    for i in range(n):
        if(s[i]=='.'):
            continue
        if(s[i]=='x'):
            y=0
            for j in range(1,k+1):
                if(i+j<n and s[i+j]=='x'):
                    y=1
                    break
                elif(i+j>=n):
                    y=1
                    break
            if(y==0):
                for j in range(i+k,i,-1):
                    if(j<n and s[j]=='*'):
                        s[j]='x'
                        a+=1
                        break
    print(a)
        
    
