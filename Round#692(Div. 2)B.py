def find(k):
    while(1):
        n=k
        while(n>0):
            r=n%10
            if(r!=0 and k%r!=0):
                break
            n=n//10
        if(n==0):
            return(k)
            break
        k+=1
t=int(input())
for _ in range(t):
    n=int(input())
    print(find(n))
    
    
