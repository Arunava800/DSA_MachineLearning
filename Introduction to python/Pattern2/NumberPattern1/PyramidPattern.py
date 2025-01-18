terms = int(input())
rows = 1
while rows <= terms:
    spaces = terms - rows
    s_cols = 1
    while s_cols <= spaces:
        print("", end=" ")
        s_cols += 1
    cols = rows
    while cols > 0:
        print(cols, end="")
        cols -= 1
    n_cols = 2
    while n_cols <= rows:
        print(n_cols, end="")
        n_cols += 1
    print()
    rows += 1
