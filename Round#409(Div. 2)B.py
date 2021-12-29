x=input()
y=input()
flag=True
for i in range(len(x)):
    if(x[i]<y[i]):
        flag=False
        break
if(flag):
    print(y)
else:
    print(-1)
