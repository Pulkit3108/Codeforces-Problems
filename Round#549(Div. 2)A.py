n=int(input())
a=list(map(int,input().split()))
c0=a.count(0)
c1=a.count(1)
c3=0
c4=0
for i in range(0,n):
    if(a[i]==0):
        c3+=1
    else:
        c4+=1
    if(c3==c0 or c4==c1):
        break
print(i+1)
