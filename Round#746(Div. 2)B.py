from sys import stdin, stdout 
input = stdin.readline
for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    if(n>=(2*x)):
        print('YES')
    else:
        b=sorted(a)
        flag=True
        for i in range(n):
            if(a[i]!=b[i]):
                if(n-1-i<x and i<x):
                    flag=False
                    break
        if(flag):
            print('YES')
        else:
            print('NO')
