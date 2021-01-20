t=int(input())
for i in range(t):
    n=int(input())
    b=input()
    s=[0]*len(b)
    a=[0]*len(b)
    a[0]=1
    if(b[0]=='0'):
        s[0]=1
    elif(b[0]=='1'):
        s[0]=2
    for i in range(1,len(b)):
        if(b[i]=='0' and b[i-1]=='0' and s[i-1]==0):
            a[i]=1
        elif(b[i]=='0' and b[i-1]=='0' and s[i-1]==1):
            a[i]=0
        elif(b[i]=='0' and b[i-1]=='1' and s[i-1]==1):
            a[i]=0
        elif(b[i]=='0' and b[i-1]=='1' and s[i-1]==2):
            a[i]=1
        elif(b[i]=='1' and b[i-1]=='1' and s[i-1]==1):
            a[i]=1
        elif(b[i]=='1' and b[i-1]=='1' and s[i-1]==2):
            a[i]=0
        elif(b[i]=='1' and b[i-1]=='0'):
            a[i]=1
        s[i]=a[i]+int(b[i])
    print(''.join(map(str,a)))
