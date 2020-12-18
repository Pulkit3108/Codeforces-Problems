n=int(input())
s=['Power','Time','Space','Soul','Reality','Mind']
for _ in range(n):
    i=input()
    if(i=='purple'):
        s.remove('Power')
    elif(i=='green'):
        s.remove('Time')
    elif(i=='blue'):
        s.remove('Space')
    elif(i=='orange'):
        s.remove('Soul')
    elif(i=='red'):
        s.remove('Reality')
    elif(i=='yellow'):
        s.remove('Mind')
print(len(s))
for i in range(len(s)):
    print(s[i])
    
