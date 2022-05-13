import sys
def compare(a,b,m):
    c=0
    for i in range(m):
        c+=abs(ord(a[i])-ord(b[i]))
    return c
for _ in range(int(input())):
    n,m=map(int,input().split())
    s=list()
    for i in range(n):
        s.append(input())
    mc=sys.maxsize
    for i in range(n):
        for j in range(i+1,n):
            mc=min(mc,compare(s[i],s[j],m))
    print(mc)
    
    
        
        
    
    
