t=int(input())
for _ in range(t):
    n=int(input())
    r=input()
    b=input()
    nr=0
    nb=0
    for i in range(n):
        if(int(r[i])>int(b[i])):
            nr+=1
        elif(int(r[i])<int(b[i])):
            nb+=1
    if(nr>nb):
        print('RED')
    elif(nb>nr):
        print('BLUE')
    else:
        print('EQUAL')
