n=int(input())
if(n&1):
    print(n//2,n//2+1)
elif(n%4==0):
    print(n//2-1,n//2+1)
else:
    print(n//2-2,n//2+2)
