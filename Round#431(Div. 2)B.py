n=int(input())
y=list(map(int,input().split()))
flag=False
for i in range(1,n):
    st=set()
    xd=i
    yd=y[i]-y[0]
    st.add(y[0]*xd)
    for j in range(n):
        st.add(y[j]*xd-(yd*j))
    if(len(k)==2):
        flag=True
        break
xd=1
yd=y[2]-y[1]
st=set()
st.add(y[1]*xd-yd)
for j in range(n):
    st.add(y[j]*xd-(yd*j))
if(len(k)==2):
    flag=True
if(flag):
    print('Yes')
else:
    print('No')
