for _ in range(int(input())):
    s=list(input())
    if(len(s)==2):
        print(int(s[1]))
    else:
        print(int(min(s)))
