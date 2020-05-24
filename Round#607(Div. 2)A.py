T=int(input())
for _ in range(0,T):
    s=input()
    if(s.endswith("po")):
        print("FILIPINO")
    if(s.endswith("desu") or s.endswith("masu")):
        print("JAPANESE")
    if(s.endswith("mnida")):
        print("KOREAN")
    
