def calc(s,i,j,k):
    c=0
    while(i>-1 and j<n):
        if(s[i]==s[k] and s[j]==s[k]):
            c+=2
        else:
            break
        i-=1
        j+=1
    return c
for _ in range(int(input())):
    n=int(input())
    s=input()
    c=0
    k=int(n/2)
    if(n&1):
        c=1+calc(s,k-1,k+1,k)   
    else: 
        c=calc(s,k-1,k,k)  
    print(c)
