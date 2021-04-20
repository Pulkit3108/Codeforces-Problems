import math
def sq(n):
    k=int(math.sqrt(n))
    if(n!=k*k):
        return True
    return False
    
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=1
    for i in range(n):
        if(sq(a[i])):
            c=0
            break
    if(c==0):
        print('YES')
    else:
        print('NO')
        
    
