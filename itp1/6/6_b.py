n = int(input()) # 持ってるカードの枚数

pattern = ["S","H","C","D"]
cards = [[False for i in range(13)] for j in range(4)]
cnt = 0

while True:
    if cnt >= n:
        break

    a, b = input().split()

    for i in range(4):
        if a == pattern[i]:
            cards[i][int(b)-1] = True
    cnt += 1;

for i in range(4):
    for j in range(13):
        if cards[i][j] == False:
            print(pattern[i], j+1)
