for _ in range(int(input())):
    n,c=input().split()
    n=int(n)
    s=input()
    f=0
    if(s.count(c)==n):
        print(0)
    else:
        k=-1
        for i in range(n-1,-1,-1):
            if(s[i]==c):
                k=i
                break
        if(k>0 and k>=n//2):
            print(1)
            print(k+1)
        else:
            print(2)
            print(n-1,n)
      
                
