n,p=map(int, input().split())
s=input()
t=s.replace('.', '0')
if(all(t[i] == t[i + p] for i in range(n - p))):
    k=-1
    for r in range(p - 1, -1, -1):
        x=s[r::p].rfind('.')
        if(x!=-1 and s[r::p]!='.'):
            k=max(k,x*p+r)
    if(k==-1):
        print('No')
    else:
        print(t[:k]+'1'+t[(k+1):])
else:
    print(t)
