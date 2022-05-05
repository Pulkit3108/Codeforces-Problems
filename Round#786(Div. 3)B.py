def ch(c):
    return ord(c)-ord('a')
for _ in range(int(input())):
    s=input()
    i=ch(s[0])*25+ch(s[1])
    if(ch(s[0])>ch(s[1])):
        i+=1
    print(i)
    
    
    
