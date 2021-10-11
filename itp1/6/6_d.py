n, m = map(int,input().split())

a = [list(map(int,input().split())) for i in range(n)]
b = [int(input()) for i in range(m)]
c = [0 for i in range(n)]

for i in range(n):
    for j in range(m):
        c[i] += a[i][j]*b[j]

for i in range(n):
    print(c[i])
