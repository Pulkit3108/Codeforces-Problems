t=int(input())
for _ in range(t):
    s=input()
    t=input()
    for i in s:
        if(i in t):
            print("YES")
            break
    else:
        print("NO")
