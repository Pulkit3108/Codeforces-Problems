''''def Swap(list, pos1, pos2): 
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list
T=int(input())
for _ in range(0,T):
    s,c=input().split()
    A=list(s)
    B=list(A)
    A.sort()
    x=0
    for i in range(0,len(s)):
        if(s[i]!=A[i]):
            a=B[i:len(s)].index(A[i])
            x=1
            break
    if(x==1):
        B=Swap(B,i+a,i)
    s1=""
    for q in B:
        s1+=q
    if(s1<c):
        print(s1)
    else:
        print("---")'''
        
def solve(s, t):
    mns = list(s)
    for i in range(len(s)-2,-1,-1): mns[i] = min(mns[i], mns[i + 1])
    for i in range(len(s)):
        if s[i] != mns[i]:
            j = max(j for j, v in enumerate(s[i:], i) if v == mns[i])
            s = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
            break
    return s if s < t else '---'

for cas in range(int(input())):
    print(solve(*input().split()))
    
