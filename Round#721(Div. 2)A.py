import math
def setBit(n):
    k=int(math.log(n,2))
    return(1<<k)
for _ in range(int(input())):
    n=int(input())
    print(setBit(n)-1)
    
