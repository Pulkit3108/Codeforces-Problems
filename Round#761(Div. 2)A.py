for _ in range(int(input())):
    s=input()
    t=input()
    s=sorted(s)
    f=[0]*26
    for i in s:
        f[ord(i)-ord('a')]+=1
    if(t!='abc' or f[0]==0 or f[1]==0 or f[2]==0):
        print(''.join(s))
    else:
        print('a'*f[0],end='')
        print('c'*f[2],end='')
        print('b'*f[1],end='')
        for i in range(3,26):
            print(chr(ord('a')+i)*f[i],end='')
        print()
