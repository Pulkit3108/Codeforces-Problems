t=int(input())
for _ in range(t):
    n=int(input())
    s='989'
    s1='0123456789'
    a=''
    if(n<=len(s)):
        a=s[:n]
    else:
        a=s
        k=(n-3)//10
        r=(n-3)%10
        a+=s1*k
        a+=s1[:r]     
    print(a)
