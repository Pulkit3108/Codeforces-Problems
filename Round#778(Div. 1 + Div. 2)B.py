for _ in range(int(input())):
    s=input()
    a=[0]*26
    for i in range(len(s)):
        a[ord(s[i])-ord('a')]+=1
    k=0
    for i in range(len(s)):
        if(a[ord(s[i])-ord('a')]>1):
            a[ord(s[i])-ord('a')]-=1
            k=i+1
        else:
            break
    print(s[k:])
        
    
