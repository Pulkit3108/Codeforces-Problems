s=input()
c=0
a=['ABC','ACB','BAC','BCA','CAB','CBA']
for i in range(6):
    if(a[i] in s):
        c=1
        break
if(c==0):
    print('No')
else:
    print('Yes')
