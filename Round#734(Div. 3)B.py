for _ in range(int(input())):
    s=input()
    f=[0]*26
    for i in s:
        f[ord(i)-ord('a')]+=1
    c=0
    for i in f:
        if(i==1):
            c+=1
        elif(i>1):
            c+=2
    print(c//2)
