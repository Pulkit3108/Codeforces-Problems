for _ in range(int(input())):
    s=input()
    st=list()
    for i in range(len(s)):
        if(s[i] not in st):
            st.append(s[i])
    flag=True
    for i in range(len(s)):
        if(s[i]!=st[i%len(st)]):
            flag=False
    if(flag):
        print('YES')
    else:
        print('NO')
    
   
    
    
    
