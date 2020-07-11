t=int(input())
for _ in range(0,t):
    l1,r1,l2,r2=map(int,input().split())
    if(l1!=l2):
        print(l1,l2)
    elif(l1!=r2):
        print(l1,r2)
    elif(r1!=l2):
        print(r1,l2)
    elif(r1!=r2):
        print(r1,r2)
    
   
