f=0
for i in range(int(input())):
    s=input()
    if(s=="Tetrahedron"):
        f+=4
    elif(s=="Cube"):
        f+=6
    elif(s=="Octahedron"):
        f+=8
    elif(s=="Dodecahedron"):
        f+=12
    else:
        f+=20
print(f)
