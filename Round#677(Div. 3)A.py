t=int(input())
for _ in range(t):
    x=input()
    a=len(x)
    a=a*(a+1)//2
    print(a+(int(x[0])-1)*10)
