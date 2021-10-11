string = input()
n = int(input())

for i in range(n):
    info = input().split()
    command = info[0]
    a = int(info[1])
    b = int(info[2]) + 1

    if command == "print":
        print(string[a:b])
    elif command == "reverse":
        string = string[:a] + string[a:b][::-1] + string[b:]
    else:
        p = info[3]
        string = string[:a] + p + string[b:]
