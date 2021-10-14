for _ in range(int(input())):
    a,b,c=map(int,input().split())
    print(max(0,1+max(b,c)-a),max(0,1+max(ac)-b),max(0,1+max(a,b)-c))
