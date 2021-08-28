p=[0]*101
for i in range(2,101):
    if(p[i]^1):
        for j in range(i*i,101,i):
            p[j]=1
for _ in range(int(input())):
    k=int(input())
    s=input()
    flag=True
    for i in s:
        if(i=='1' or i=='4' or i=='6' or i=='8' or i=='9'):
            print(1)
            print(i)
            flag=False
            break
    if(flag):
        flag=False
        for i in range(k):
            for j in range(i+1,k):
                if(p[(ord(s[i])-ord('0'))*10+(ord(s[j])-ord('0'))]):
                    print(2)
                    print(s[i],end='')
                    print(s[j])
                    flag=True
                    break
            if(flag):
                break
                
            
            
    

    
