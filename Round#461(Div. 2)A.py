x,y=map(int,input().split())
x1=x-y+1
if(y==0 or (x1==x and x!=0) or x1<0 or x1%2!=0):
    print('No')
else:
    print('Yes')
