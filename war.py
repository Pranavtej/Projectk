def fun(m, n, t, ci, rp):
    bf = [['z' for _ in range(n)] for _ in range(m)] 
    ti = 0
    for row in range(m):
        start_idx = rp[row]
        end_idx = rp[row + 1]
        for i in range(start_idx, end_idx):
            col = ci[i]
            bf[row][col] = t[ti]
            ti += 1 
    return bf
m = int(input())
n = int(input())
ti = input()
t = list(ti.split())
ci = list(map(int, input().split()))
rp = list(map(int, input().split()))
res = fun(m, n, t, ci, rp)
for row in res:
    print(" ".join(row))