s=input()
h=int(s[:2])
m=int(s[3:])
t=0
while((h%10)!=(m//10) or (h//10)!=(m%10)):
    m+=1
    h+=m//60
    m=m%60
    h=h%24
    t+=1
print(t)
