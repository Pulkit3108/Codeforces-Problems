t=int(input())
for _ in range(0,t):
    n=int(input())
    s=input()
    c=0
    op=0
    ed=0
    for i in s:
        if(i=='('):
            op+=1
        else:
            ed+=1
        if(op==ed):
            op=0
            ed=0
        elif(ed>op):
            ed=0
            op=0
            c+=1
        else:
            continue
    print(c)
