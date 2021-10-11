r, c = map(int,input().split())
table = [list(map(int,input().split())) for i in range(r)]

for i in range(r):
    total = 0
    for j in range(c):
        total += table[i][j]
        print(table[i][j],end=" ")
    print(total)

all_total = 0
for i in range(c):
    total = 0
    for j in range(r):
        total += table[j][i]
    all_total += total
    print(total,end=" ")
print(all_total)
