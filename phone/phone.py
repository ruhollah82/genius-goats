def num(m):
    
    if m[1:].isdigit():
        if m[0]=="0" and m[1]=="9" and len(m)==11  :
            print("+98"+m[1:])
            return True
        elif m[0]=="+" and m[1]=="9" and m[2]=="8" and len(m)==13:
            print(m)
            return True
        elif m[0]=="9" and m[1]=="8" and len(m)==12:
            print("+"+m)
            return True
    return False


n = input()
n=int(n)
lphon=[]
for i in range(n):
    m=input()
    lphon.append(m)
    
for i in lphon:
    if num(i)==False:
        print("invalid")