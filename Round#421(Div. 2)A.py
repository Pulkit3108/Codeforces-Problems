c,v0,v1,a,l=map(int,input().split())
d=1
p=v0
i=1
while(c>p):
    r=min(v0+(i*a),v1)
    c+=l
    p+=r
    i+=1
    d+=1
print(d)
