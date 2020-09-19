n,k=map(int,input().split())
ID=list(map(int,input().split()))
S=list()
for i in range(n):
    if(len(S)!=k):
        if(ID[i] not in S):
            S.append(ID[i])
        else:
            continue
    else:
        if(ID[i] not in S):
            del S[0]
            S.append(ID[i])
        else:
            continue
print(len(S))
print(' '.join(map(str,S[::-1])))
