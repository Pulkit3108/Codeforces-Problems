for _ in range(int(input())):
    n=int(input())
    c2=n//3
    c1=c2
    if(n%3==1):
        c1+=1
    elif(n%3==2):
        c2+=1
    print(c1,c2)
    

