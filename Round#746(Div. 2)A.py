from sys import stdin, stdout 
input = stdin.readline
for _ in range(int(input())):
    n,H=map(int,input().split())
    a=list(map(int,input().split()))
    m1=max(a)
    a.remove(m1)
    m2=max(a)
    if(H%(m1+m2)==0):
        print(2*(H//(m1+m2)))
    elif(H%(m1+m2)>m1):
        print((2*(H//(m1+m2)))+2)
    else:
        print((2*(H//(m1+m2)))+1)
