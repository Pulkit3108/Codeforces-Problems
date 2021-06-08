for _ in range(int(input())):
    n=int(input())
    s=input()
    c=[0]*26
    f1=1
    f2=1
    f3=1
    for i in s:
        c[ord(i)-ord('a')]=1
    for i in range(len(c)):
        if(c[i]==0):
            print(chr(ord('a')+i))
            f1=0
            f2=0
            f3=0
            break
    if(f1):
        for i in range(26):
            for j in range(26):
                t=chr(ord('a')+i)+chr(ord('a')+j)
                if(t not in s):
                    print(t)
                    f2=0
                    f3=0
                    break
            if(f2==0):
                break
    if(f2):
        for i in range(26):
            for j in range(26):
                for k in range(26):
                    t=chr(ord('a')+i)+chr(ord('a')+j)+chr(ord('a')+k)
                    if(t not in s):
                        print(t)
                        f3=0
                        break
                if(f3==0):
                    break
            if(f3==0):
                break
        


