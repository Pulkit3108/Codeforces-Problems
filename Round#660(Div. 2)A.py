t=int(input())
for _ in range(0,t):
    n=int(input())
    if(n>30):
        print("YES")
        if(n==36 or n==40 or n==44):
            print(6,10,15,n-31)
        else:
            print(6,10,14,n-30);
    else:
        print("NO")
            
