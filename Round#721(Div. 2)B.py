for _ in range(int(input())):
    n=int(input())
    s=input()
    k=s.count('0')
    if(k%2==0 or k==1):
        print('BOB')
    else:
        print('ALICE')
    
