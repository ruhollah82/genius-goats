m,n = input().split()

n = int(n)
m = int(m)

if n-m > 0 :
    for i in range(n-m):
        print("R",end="")

elif m-n > 0 :
    for i in range(m-n):
        print("L",end="")
        
else :
    print("Saal Noo Mobarak!")