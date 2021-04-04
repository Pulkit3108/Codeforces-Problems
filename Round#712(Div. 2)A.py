def rev(s):
    return(s[::-1])
for _ in range(int(input())):
    s=input()
    if(s.count('a')==len(s)):
        print('NO')
    elif(s==rev(s)):
        print('YES')
        print(s+'a')
    else:
        print('YES')
        k=s+'a'
        if(k!=rev(k)):
            print(k)
        else:
            print('a'+s)
