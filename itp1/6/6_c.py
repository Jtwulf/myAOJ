n = int(input())

b = list(range(n))  # 棟
f = list(range(n))  # 階
r = list(range(n))  # 部屋
v = list(range(n))  # 人数

s = [0,0,0,0,0,0,0,0,0,0]

for i in range(n):
    b[i], f[i], r[i], v[i] = map(int, input().split())

for i in range(4):  # 4棟分の繰り返し
    for j in range(3):  # 3階分の繰り返し
        for k in range(10):  # 10部屋分の繰り返し
            for l in range(n):  # データ件数分の繰り返し
                if b[l] == i+1 and f[l] == j+1 and r[l]== k+1:
                    s[k] = s[k] + v[l]
        print('', *s)
        s[:] = [0,0,0,0,0,0,0,0,0,0]
    if i != 3:
        print("####################")
