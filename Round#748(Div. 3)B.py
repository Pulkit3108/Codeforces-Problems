import sys
for _ in range(int(input())):
    s=list(map(int,input()))
    n=len(s)
    m=sys.maxsize      
    for i in range(n):
        for j in range(i+1,n):
            if(s[j]==0):
                if(s[i]==0 or s[i]==5):
                    m=min(m,j-i)+n-j-1
            elif(s[j]==5):
                if(s[i]==2 or s[i]==7):
                    m=min(m,j-i)+n-j-1
    print(m-1)
