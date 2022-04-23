for _ in range(int(input())):
    r=int(input())
    if(1900<=r):
        print('Division 1')
    elif(1600<=r and r<=1899):
        print('Division 2')
    elif(1400<=r and r<=1599):
        print('Division 3')
    elif(r<=1399):
        print('Division 4')
