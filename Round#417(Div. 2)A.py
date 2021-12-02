l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=list(map(int,input().split()))
l4=list(map(int,input().split()))
flag=False
if(l1[3]==1):
    if(l1.count(1)>1 or l2[0]==1 or l3[1]==1 or l4[2]==1):
        flag=True
if(l2[3]==1):
    if(l1[2]==1 or l2.count(1)>1 or l4[1]==1 or l3[0]==1):
        flag=True
if(l3[3]==1):
    if(l1[1]==1 or l2[2]==1 or l3.count(1)>1 or l4[0]==1):
        flag=True
if(l4[3]==1):
    if(l1[0]==1 or l2[1]==1 or l3[2]==1 or l4.count(1)>1):
        flag=True
if(flag):
    print("YES")
else:
    print("NO")
    
