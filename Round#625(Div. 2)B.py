n=int(input())
b=list(map(int,input().split()))
po=[0]*1000001
ne=[0]*1000001
for i in range(n):
    if((i+1-b[i])>0):
        po[abs(i+1-b[i])]+=b[i]
    else:
        ne[abs(i+1-b[i])]+=b[i]
print(max(max(po),max(ne)))


