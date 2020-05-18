def cal(n):
    if(n==1):
        return(1)
    else:
        return(4*(n-1)+cal(n-1))
n=int(input())
print(cal(n))
