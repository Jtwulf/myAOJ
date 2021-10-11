W = input().lower()
ans = 0
T = ""

while T != "END_OF_TEXT":
    T = input()
    ans += T.lower().split().count(W)

print(ans)
