n,k=map(int,input().split())
S=input()
A=list(S)
if(k==0):
    print(S)
else:
    if(n==1):
        print(0)
    else:
        for j in range(0,n):
            if(j==0):
                if(A[j]!='1'):
                    break
            else:
                if(A[j]!='0'):
                    break
        i=j
        k=k+j
        while(j<k):
            if(i>=n):
                break
            else:
                if(i==0):
                    A[i]='1'
                    j+=1
                if(A[i]!='0' and i!=0):
                    A[i]='0'
                    j+=1
            i+=1
        print(''.join(map(str,A)))

