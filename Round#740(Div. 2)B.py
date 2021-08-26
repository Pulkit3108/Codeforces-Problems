for _ in range(int(input())):
    a,b=map(int,input().split())
    l=a+b
    o=(a+b)//2
    e=a+b-o
    st=list()
    for i in range(0,o+1):
        a0=i
        a1=a-i
        b0=o-a0
        b1=e-a1
        if(a0<0 or a1<0 or b0<0 or b1<0):
            continue
        else:
            st.append(a0+b1)
    for i in range(0,e+1):
        a0=a-i
        a1=i
        b0=o-a0
        b1=e-a1
        if(a0<0 or a1<0 or b0<0 or b1<0):
            continue
        else:
            st.append(a1+b0)
    st=list(set(st))
    st.sort()
    print(len(st))
    print(' '.join(map(str,st)))
            
    

    
    
