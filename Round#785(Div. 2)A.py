def getVal(c):
    return (ord(c)-ord('a')+1)
for _ in range(int(input())):
    s=input()
    n=len(s)
    if(n==1):
        print('Bob',getVal(s))
    else:
        a=0
        for i in s:
            a+=getVal(i)
        if(n&1):
            print('Alice',a-2*min(getVal(s[0]),getVal(s[n-1])))
        else:
            print('Alice',a)
    
    
    
