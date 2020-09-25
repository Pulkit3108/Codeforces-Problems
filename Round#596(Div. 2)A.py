da,db=map(int,input().split())
if(da==9 and db==1):
    print(9,10)
elif(abs(da-db)>1 or da>db):
    print(-1)
elif(da==db):
    print("{}1 {}2".format(da,db))
else:
    print("{}9 {}0".format(da,db))
