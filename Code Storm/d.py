import sys
sys.setrecursionlimit(10000)

def count_self_products(A, B):
    count = 0

    def dfs(p, n, k):
        nonlocal count
        if n != 0:
            khodmaz = n * k
            if khodmaz > B:
                return  
            if A <= khodmaz <= B:
                count += 1

    
        for d in range(1, 10):  
            new_n = n * 10 + d
            new_k = k * d
            if new_n > 0 and new_n * new_k > B:
                continue  
            dfs(p + 1, new_n, new_k)

    dfs(0, 0, 1)
    return count


A, B = map(int, input().split())
print(count_self_products(A, B))