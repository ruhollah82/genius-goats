import math
MOD = 10**9 + 7
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

d_v = [[0]*n for _ in range(n)]
d_l = [[-float('inf')]*n for _ in range(n)]

if m[0][0] > 0:
    d_v[0][0] = m[0][0]
    d_l[0][0] = math.log(m[0][0])
else:
    d_v[0][0] = 0
    d_l[0][0] = -float('inf')

for j in range(1, n):
    if m[0][j] == 0 or d_l[0][j-1] == -float('inf'):
        d_v[0][j] = 0
        d_l[0][j] = -float('inf')
    else:
        d_v[0][j] = (d_v[0][j-1] * m[0][j]) % MOD
        d_l[0][j] = d_l[0][j-1] + math.log(m[0][j])

for i in range(1, n):
    if m[i][0] == 0 or d_l[i-1][0] == -float('inf'):
        d_v[i][0] = 0
        d_l[i][0] = -float('inf')
    else:
        d_v[i][0] = (d_v[i-1][0] * m[i][0]) % MOD
        d_l[i][0] = d_l[i-1][0] + math.log(m[i][0])

for i in range(1, n):
    for j in range(1, n):
        up_log = d_l[i-1][j]
        left_log = d_l[i][j-1]

        if m[i][j] == 0:
            d_v[i][j] = 0
            d_l[i][j] = -float('inf')
        elif up_log > left_log:
            d_v[i][j] = (d_v[i-1][j] * m[i][j]) % MOD
            d_l[i][j] = up_log + math.log(m[i][j])
        else:
            d_v[i][j] = (d_v[i][j-1] * m[i][j]) % MOD
            d_l[i][j] = left_log + math.log(m[i][j])

print(d_v[-1][-1])