n=int(input())
a=list(map(int,input().split()))
b=[ i-1 if i%2==0 else i for i in a ]
print(' '.join(map(str,b)))
