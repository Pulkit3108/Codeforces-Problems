for _ in range(int(input())):
    _=input()
    b=list()
    for i in range(8):
        b.append(input())
    x,y=0,0
    for i in range(1,7):
        for j in range(1,7):
            if(b[i-1][j-1]=='#' and b[i-1][j+1]=='#' and b[i+1][j+1]=='#' and b[i+1][j-1]=='#'):
                x,y=i+1,j+1
    print(x,y)
