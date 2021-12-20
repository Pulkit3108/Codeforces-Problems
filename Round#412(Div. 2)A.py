n=int(input())
r=list()
for _ in range(n):
    i=list(map(int,input().split()))
    r.append(i)
f=2
for i in range(n):
    if(r[i][0]==r[i][1]):
        for j in range(n):
            if(i<j and r[i][0]<r[j][0]):
                f=0
                break
        if(f==0):
            break
for i in range(n):
    if(r[i][0]!=r[i][1]):
        f=1
        break        
if(f==0):
    print('unrated')
elif(f==1):
    print('rated')
else:
    print('maybe')
    
        
    
