import math
t=int(input())
for _ in range(t):
    w,h,n=map(int,input().split())
    c=0
    if(w%2==0 and h%2!=0):
        s=w
        while(s%2==0):
            c+=1
            s=s//2
        c=math.pow(2,c)
    elif(h%2==0 and w%2!=0):
        s=h
        while(s%2==0):
            c+=1
            s=s//2
        c=math.pow(2,c)
    elif(w%2==0 and h%2==0):
        s=w
        while(s%2==0):
            c+=1
            s=s//2
        s=h
        while(s%2==0):
            c+=1
            s=s//2
        c=math.pow(2,c)
    if(c>=n or n==1):
        print("YES")
    else:
        print("NO")
