t=int(input())
for _ in range(0,t):
    n=int(input())
    s=input()
    c1=0
    c2=0
    for i in range(0,n):
        if(s[i]=='0'):
            c1+=1
        else:
            break
    for j in range(n-1,-1,-1):
        if(s[j]=='1'):
            c2+=1
        else:
            break
    ans=""
    if((abs(i-j)==1 and i>j) or c1==n or c2==n):
        ans+='0'*c1
        ans+='1'*c2
    else:
        ans+='0'*(c1+1)
        ans+='1'*c2
    print(ans)
