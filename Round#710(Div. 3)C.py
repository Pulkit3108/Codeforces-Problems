def lstring(x,y):
    m=len(x)
    n=len(y)
    dp=[[0 for k in range(n+1)] for l in range(m+1)]
    r=0
    for i in range(m+1):
        for j in range(n+1):
            if(i==0 or j==0):
                dp[i][j]=0
            elif(x[i-1]==y[j-1]):
                dp[i][j]=dp[i-1][j-1]+1
                r=max(r,dp[i][j])
            else:
                dp[i][j]=0
    return(r) 
t=int(input())
for _ in range(t):
    a=input()
    b=input()
    l=lstring(a,b)
    print(len(a)-l+len(b)-l)
    
