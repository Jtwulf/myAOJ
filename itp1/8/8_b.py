while True:
    x = int(input())
    sum = 0
    if x == 0:
        break
    while x > 0:
        sum += x % 10
        x //= 10
    print(sum)
