def dist(a,b,c,d):
    return(abs(a*d-b*c))
ax,ay,bx,by,cx,cy=map(int,input().split())
if(((ax-bx)**2 + (ay-by)**2 == (cx-bx)**2 + (cy-by)**2) and dist(ax-bx,ay-by,cx-bx,cy-by)>0):
    print('Yes')
else:
    print('No')
