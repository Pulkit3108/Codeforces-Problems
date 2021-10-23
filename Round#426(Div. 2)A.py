d=['v','<','^','>']
s,e=input().split()
n=int(input())
t=(d.index(e)-d.index(s)+4)%4
if(t==0 or t==2):
    print('undefined')
elif(t==n%4):
    print('cw')
else:
    print('ccw')
