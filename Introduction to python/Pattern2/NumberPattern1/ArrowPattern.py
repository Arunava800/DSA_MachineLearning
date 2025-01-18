terms = int(input())
rows_1 = terms // 2
rows_2 = rows_1 - 1
rows = 1
while rows <= rows_1:
    spaces = 1
    while spaces <= rows - 1:
        print("", end=" ")
        spaces += 1
    cols = 1
    while cols <= rows:
        print("*", end="")
        cols += 1
    print()
    rows += 1
