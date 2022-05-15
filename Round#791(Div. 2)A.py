import math
for _ in range(int(input())):
    n=int(input())
    if(n<3 or n&1):
        print(-1)
    else:
        n=n//2
        print(n//3+(n%3>0),n//2)
        
    
    
    
        
        
    
    
