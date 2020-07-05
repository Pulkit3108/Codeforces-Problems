def f(x):
    x+=1
    while(x%10==0):
        x//=10
    return(x)
a=list()
n=int(input())
while(n not in a):
    a.append(n)
    n=f(n)
print(len(a))
