n=int(input())
s=list(input().split())
t=set()
for i in s:
    k=len(i)
    c=0
    for j in range(k):
        c=c | (1<<(ord(i[j])-ord('a')))
    # print(c)
    t.add(c)
print(len(t))


