S = str(input())
P = str(input())

is_ok = False

for i in range(len(S)):
    flag = True
    for j in range(len(P)):
        print(S[(i+j)%(len(S))])
        if S[(i+j)%(len(S))] != P[j]:
            flag = False
            break

    if flag == True:
        is_ok = True
        break

if is_ok == True:
    print("Yes")
else:
    print("No")
