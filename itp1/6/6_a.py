n = int(input())
a = list(map(int,input().split()))

a.reverse()

# print(" ".join(map(str,a)))

for i, elem in enumerate(a):
    if i > 0:
        print(" ", end = "")
    print(elem, end = "")
print()
