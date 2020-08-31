from collections import Counter 
t=int(input())
for _ in range(t):
    S=list()
    n=int(input())
    for i in range(n):
        S.append(input())
    A=[0]*26
    for i in range(n):
        for j in range(len(S[i])):
            A[ord(S[i][j])-ord('a')]+=1
    c=1
    for i in A:
        if(i%n!=0):
            c=0
            break
    if(c==0):
        print("NO")
    else:
        print("YES")
    
