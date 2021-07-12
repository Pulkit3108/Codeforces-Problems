for _ in range(int(input())):
    _ = input()
    xa,ya=map(int,input().split())
    xb,yb=map(int,input().split())
    xf,yf=map(int,input().split())
    c=abs(xa-xb)+abs(ya-yb)
    if((xa==xb and xb==xf) and ((yf>ya and yf<yb) or (yf<ya and yf>yb))):
        c+=2
    if((ya==yb and yb==yf) and ((xf>xa and xf<xb) or (xf<xa and xf>xb))):
        c+=2
    print(c)
