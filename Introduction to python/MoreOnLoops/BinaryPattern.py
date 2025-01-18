terms = int(input())
rows = 1
flag = True
for i in range(terms, 0, -1):
    if flag:
        for j in range(i, 0, -1):
            print("1", end="")
        flag = False
    else:
        for j in range(i, 0, -1):
            print("0", end="")
        flag = True

    print()
