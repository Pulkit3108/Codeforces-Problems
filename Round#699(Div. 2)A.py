t=int(input())
for _ in range(t):
    px,py=map(int,input().split())
    s=input()
    u=d=l=r=0
    for i in s:
        if(i=='U'):
            u+=1
        elif(i=='D'):
            d+=1
        elif(i=='L'):
            l+=1
        elif(i=='R'):
            r+=1
    if((px<0 and abs(px)>l) or (px>0 and px>r) or (py<0 and abs(py)>d) or (py>0 and abs(py)>u)):
        print('NO')
    else:
        print('YES')

