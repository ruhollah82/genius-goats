x = input()
x = int(x)

m,n = input().split()
m = int(m)
n = int(n)

if x == 1:
    print(int(m + n))
elif x == 2:
    print(n-m) 
elif x == 3:
    print(m-n)
elif x == 4:
    print(int(m*n))   
    