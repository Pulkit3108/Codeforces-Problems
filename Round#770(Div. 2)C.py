for _ in range(int(input())):
    n,k=map(int,input().split())
    if(k>1 and n&1):
        print("NO")
    else:
        print("YES")
        if(k==1):
            for i in range(1,n+1):
                print(i)
        else:
            for i in range(1,n+1):
                for j in range(i,(n*k)+1,n):
                    print(j,end=' ')
                print()





        
