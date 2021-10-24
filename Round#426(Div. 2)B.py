n,k=map(int,input().split())
s=input()
f=[0]*26
for i in range(n):
    f[ord(s[i])-ord('A')]=i
st=set()
flag=False
for i in range(n):
    st.add(s[i])
    if(len(st)>k):
        flag=True
        break
    if(f[ord(s[i])-ord('A')]==i):
        st.remove(s[i])
if(flag):
    print('YES')
else:
    print('NO')
