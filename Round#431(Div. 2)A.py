n=int(input())
a=list(map(int,input().split()))
if(len(a)%2==0):
    print('No')
else:
    if(a[0]&1 and a[-1]&1):
        print('Yes')
    else:
        print('No')
