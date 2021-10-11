N = int(input())
x = 0
y = 0

for i in range(N):
    a, b = input().split()
    if a < b:
        y += 3
    elif b < a:
        x += 3
    else:
        x += 1
        y += 1
print(x,y)
