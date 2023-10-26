L, W = map(int, input().split()) 

A = [[0 for i in range(W)] for j in range(L)]

for i in range(L):
    A[i] = list(map(int, input().split()))[:W] 

H = int(input())

r, c = 0, 0
for i in range(L):
    for j in range(W):
        if A[i][j] <= H:
            r, c = i, j       
print(r, c+1)