t= int(input())
for _ in range(0,t):
    s=int(input())
    c=0
    x=s
    while(x!=0):
        r=x%10
        q=x//10
        if(q==0):
            x=0
            c+=r
        else:
            x=q+r
            c+=q*10
    print(c)




    
