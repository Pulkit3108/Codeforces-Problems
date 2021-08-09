a=list(map(int,input().split()))
s=sum(a)
if(s%2!=0):
    print('NO')
else:
    s=s//2
    flag=False
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            for k in range(j+1,len(a)):
                if(a[i]+a[j]+a[k]==s):
                    flag=True
                    break
            if(flag):
                break
        if(flag):
            break
    if(flag):
        print('YES')
    else:
        print('NO')
