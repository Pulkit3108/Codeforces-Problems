A,B=map(int,input().split())
x,y,z=list(map(int,input().split()))
print(max(0,x*2+y-A)+max(0,z*3+y-B))
