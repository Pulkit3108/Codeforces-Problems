n,m=map(int,input().split())
name=list()
ip1=list()
for i in range(n):
    a,b=input().split()
    name.append(a)
    ip1.append(b)
cmd=list()
ip2=list()
for i in range(m):
    a,b=input().split()
    cmd.append(a)
    ip2.append(b)
s=list()
for i in range(m):
    s.append(cmd[i]+' '+ip2[i]+' ''#'+name[ip1.index(ip2[i][:-1])])
for i in s:
    print(i)
