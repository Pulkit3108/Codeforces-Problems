s=input()
if(len(s)<4):
    print('No')
else:
    d=0
    c=0
    a=[0]*26
    for i in s:
        if(a[ord(i)-ord('a')]==0):
            d+=1
        a[ord(i)-ord('a')]+=1
    if(d==4 or d==3 or (d==2 and (1 not in a))):
        c=1
    if(c==0):
        print('No')
    else:
        print('Yes')
    
