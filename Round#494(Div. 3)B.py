a,b,x=map(int,input().split())
s=''
if(x==1):
    s='0'*a+'1'*b
else:
    if(a>b):
        for i in range(x):
            if(i%2==0):
                s+='0'
            else:
                s+='1'
        if(s[0]!=s[len(s)-1]):
            s=s+'1'*(b-x//2)+'0'*(a-x//2)
        else:
            s=s+'0'*(a-x//2-1)+'1'*(b-x//2)
    else:
        for i in range(x):
            if(i%2==0):
                s+='1'
            else:
                s+='0'
        if(s[0]!=s[len(s)-1]):
            s=s+'0'*(a-x//2)+'1'*(b-x//2)
        else:
            s=s+'1'*(b-x//2-1)+'0'*(a-x//2)
print(s)
    
