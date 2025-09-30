x,y=input().split()
x=int(x)
y=int(y)
if x==y :
    print("Saal Noo Mobarak!")
while x<y :
    print("R",end="")
    x=x+1
while y<x :
    print("L", end="")
    x=x-1
