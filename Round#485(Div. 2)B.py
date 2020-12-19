import math
x,y=map(int,input().split())
if(x==y):
    print('=')
else:
    if(y*math.log(x)==x*math.log(y)):
        print('=')
    elif(y*math.log(x)<x*math.log(y)):
        print('<')
    else:
        print('>')
    
