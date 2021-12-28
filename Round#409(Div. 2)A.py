s=input()
s='K'+s+'V'
c=s.count('VK')
if('VVV' in s or 'KKK' in s):
    c+=1
print(c)
