n,m = input().split()
n = int(n)
m = int(m)
arr = [0] * n


for i in range(m):
    x,y,z = input().split()
    x = int(x)
    y = int(y)
    z = int(z)
    arr[x-1] -= z
    arr[y-1] += z
    
arr.sort()
print(arr)
