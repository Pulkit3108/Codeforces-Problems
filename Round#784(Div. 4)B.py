from collections import Counter
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    f=Counter(a)
    flag=False
    for i,c in f.items():
        if(c>2):
            flag=True
            break
    if(flag):
        print(i)
    else:
        print(-1)
    
    
