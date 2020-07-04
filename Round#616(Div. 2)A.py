t=int(input())
for _ in range(0,t):
    n=int(input())
    s=input()
    s=list(map(int,s))
    O=list()
    for i in range(0,n):
        if(s[i]%2!=0):
            O.append(s[i])          
    if(len(O)<2):
        print(-1)
    else:
        print(O[0],end='')
        print(O[1])



    


    
    


