for _ in range(int(input())):
    _=input()
    k,n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    i=0
    j=0
    c=1
    t=list()
    while(i<n or j<m):
        if(i<n and j<m):
            if(a[i]==0):
                t.append(a[i])
                i+=1
                k+=1
            elif(b[j]==0):
                t.append(b[j])
                j+=1
                k+=1
            else:
                if(a[i]<b[j] and a[i]<k+1):
                    t.append(a[i])
                    i+=1
                elif(b[j]<=a[i] and b[j]<k+1):
                    t.append(b[j])
                    j+=1
                else:
                    c=0
                    break
        elif(i<n):
            if(a[i]==0):
                t.append(a[i])
                i+=1
                k+=1
            else:
                if(a[i]<k+1):
                    t.append(a[i])
                    i+=1
                else:
                    c=0
                    break
        else:
            if(b[j]==0):
                t.append(b[j])
                j+=1
                k+=1
            else:
                if(b[j]<k+1):
                    t.append(b[j])
                    j+=1
                else:
                    c=0
                    break  
    if(c==1):
        print(' '.join(map(str,t)))
    else:
        print(-1)
            
