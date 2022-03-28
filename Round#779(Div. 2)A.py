for _ in range(int(input())):
    n=int(input())
    s=input()
    e=0
    c=2
    for i in s:
        if(i=='1'): 
            c+=1
        else:
            e+=max(2-c,0)
            c=0
    print(e)
        
    
