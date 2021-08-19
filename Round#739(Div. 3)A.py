for _ in range(int(input())):
    k=int(input())
    l=0
    while(k):
        l+=1
        while(l%3==0 or l%10==3):
            l+=1
        k-=1
    print(l)
    
