for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split())) 
    print(len(set(a))-((len(a)-len(set(a)))&1))
