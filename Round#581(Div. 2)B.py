n,l,r=map(int,input().split())
m1=pow(2,l)-1+n-l
m2=pow(2,r)-1+(n-r)*pow(2,r-1)
print(m1,m2)
