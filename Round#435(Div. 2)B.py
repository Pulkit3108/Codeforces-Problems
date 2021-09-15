from queue import Queue
n=int(input())
g=[[]*n for _ in range(n)]
for i in range(n-1):
    u,v=map(int,input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
queue=Queue()
d=[-1]*n
for i in range(n):
    if(d[i]==-1):
        d[i]=0
        queue.put(i)
        while(not queue.empty()):
            u=queue.get()
            for v in g[u]:
                if(d[v]==-1):
                    d[v]=1-d[u]
                    queue.put(v)
l=d.count(0)
r=n-l
print(l*r-(n-1))
