n=int(input())
A=list(map(int,input().split()))
E=list()
O=list()
e=0
o=0
s=0
for i in A:
    if(i%2==0):
        E.append(i)
        e+=1
    else:
        O.append(i)
        o+=1
E.sort()
O.sort()
E=E[::-1]
O=O[::-1]
if(e>o):
    A.remove(E[0])
    E.pop(0)
    for i in range(0,o):
        A.remove(E[i])
        A.remove(O[i])
elif(o>e):
    A.remove(O[0])
    O.pop(0)
    for i in range(0,e):
        A.remove(E[i])
        A.remove(O[i]) 
s=sum(A)
if(e==o):
    s=0
print(s)
