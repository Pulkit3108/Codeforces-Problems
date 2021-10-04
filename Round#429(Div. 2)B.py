n=int(input())   
a=list(map(int,input().split()))
flag=False
for i in a:
    if(i&1):
        flag=True
        break
if(flag):
    print('First')
else:
    print('Second')
