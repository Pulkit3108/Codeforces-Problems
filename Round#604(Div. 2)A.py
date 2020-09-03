t=int(input())
for _ in range(t):
    s=input()
    if(("cc" in s) or ("aa" in s) or ("bb" in s)):
        print(-1)
    else:
        s=list(s)
        n=len(s)
        i=0
        while(i<n):
            if(s[i]=="?"):
                if(i==0):
                    x='f'
                else:
                    x=s[i-1]
                if(i+1>=n):
                    y='f'
                else:
                    y=s[i+1]
                A=['a','b','c']
                for j in A:
                    if(j!=x and j!=y):
                        s[i]=j;
            else:
                i+=1
        print(''.join(map(str,s)))

            
