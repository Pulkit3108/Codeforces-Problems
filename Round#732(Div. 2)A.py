for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if(sum(a)!=sum(b)):
        print(-1)
    else:
        c=[ a[i]-b[i] for i in range(n)]
        i=0
        j=0
        ans1=list()
        ans2=list()
        while(i<n and j<n):
            if(c[i]<0 and c[j]>0):
                c[i]+=1
                c[j]-=1
                ans1.append(i+1)
                ans2.append(j+1)
            elif(c[i]<0):
                j+=1
            elif(c[j]>0):
                i+=1
            else:
                i+=1
                j+=1
        print(len(ans1))
        for i in range(len(ans1)):
            print(ans2[i],ans1[i])
