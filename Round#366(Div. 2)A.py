n=int(input())
s='I hate that I love that '
if(n==1):
    print("I hate it")
elif(n==2):
    print("I hate that I love it")
elif(n%2!=0):
    r=n//2
    print(s*r+"I hate it")
else:
    r=(n-1)//2
    print(s*r+"I hate that I love it")
