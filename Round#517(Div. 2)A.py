w,h,k=map(int,input().split())
c=0
for i in range(k):
    c+=(w-4*i)*2 + (h-4*i)*2 - 4
print(c)
