n=int(input())
s=input()
a=list(map(int,input().split()))
s=list(map(int,s))
c=1
for i in range(0,n):
    if(s[i]<a[s[i]-1]):
        c=0
        s[i]=a[s[i]-1]
    elif(s[i]>a[s[i]-1] and c==0):
        break
print(''.join(map(str,s)))
