a,b,c=map(int,input().split())
n=int(input())
x=list(map(int,input().split()))
n=0
for i in x:
    if(i>b and i<c):
        n+=1
print(n)
