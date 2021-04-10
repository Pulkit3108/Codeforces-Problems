x=int(input())
hh,mm=map(int,input().split())
t=hh*60+mm
i=0
while(1):
    h=t//60
    m=t%60
    if(h//10==7 or h%10==7 or m//10==7 or m%10==7):
        break
    t=(t-x+1440)%1440
    i+=1
print(i)
