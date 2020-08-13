def check(r,g,b,w):
    if((r%2 + g%2 + b%2 + w%2)>1):
        return(False)
    else: 
        return(True)
t=int(input())
for _ in range(t):
    r,g,b,w = map(int,input().split())
    if(check(r,g,b,w)):
        print("Yes")
    elif(r>0 and g>0 and b>0 and check(r-1,g-1,b-1,w+1)):
        print("Yes")
    else:
        print("No")
