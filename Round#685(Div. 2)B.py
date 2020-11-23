t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    s=input()
    mx=[0]*2
    mn=[0]*2
    for i in range(0,n):
        if(s[i]=='0'):
            mn[0]=i
            break
    for i in range(0,n):
        if(s[i]=='1'):
            mn[1]=i
            break
    for i in range(n-1,-1,-1):
        if(s[i]=='0'):
            mx[0]=i
            break      
    for i in range(n-1,-1,-1):
        if(s[i]=='1'):
            mx[1]=i
            break
    for _ in range(q):
        c=0
        l,r=map(int,input().split())
        l-=1
        r-=1
        if(s[l]=='0' and s[r]=='0'):
            if(l>mn[0] or r<mx[0]):
                c=1
        elif(s[l]=='1' and s[r]=='0'):
            if(l>mn[1] or r<mx[0]):
                c=1
        elif(s[l]=='1' and s[r]=='1'):
            if(l>mn[1] or r<mx[1]):
                c=1
        elif(s[l]=='0' and s[r]=='1'):
            if(l>mn[0] or r<mx[1]):
                c=1
        if(c==1):
            print("YES")
        else:
            print("NO")
            
