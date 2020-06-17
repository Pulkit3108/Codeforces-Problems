t=int(input())
for _ in range(0,t):
    s1=input()
    s2=""
    s2+=s1[0]
    for i in range(1,len(s1)-1,2):
        if(s1[i]==s1[i+1]):
            s2+=s1[i]
    s2+=s1[len(s1)-1]
    print(s2)

