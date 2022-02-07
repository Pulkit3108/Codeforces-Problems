for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    if(s==s[::-1] or k==0) :
        print(1)
    else:
        print(2)
    

        
