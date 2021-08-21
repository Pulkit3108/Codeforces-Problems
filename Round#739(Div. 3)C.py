for _ in range(int(input())):
    k=int(input())
    a=1
    i=1
    d=1
    while(k>=a+d):
        a+=d
        d+=2
        i+=1
    d=a+i-1
    if(k<=d):
        print(k-a+1,i)
    else:
        print(i,i*i-k+1)
        
    
