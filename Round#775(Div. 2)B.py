import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=sum(a)
    m=max(a)
    if(s==0):
        print(0)
    elif(2*m>s):
        print(2*m-s)
    else:
        print(1)
    
    
    



        
