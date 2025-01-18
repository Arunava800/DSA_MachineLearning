terms = int(input())
rows = 1
t_cols = (2 * terms) + 1

while rows <= terms:
    cols = 1
    while cols <= t_cols:
        if rows == cols:
            print("*", end="")
        elif rows + cols == t_cols + 1:
            print("*", end="")
        elif cols == (t_cols + 1) // 2:
            print("*", end="")
        else:
            print("0", end="")
        cols += 1
    print()
    rows += 1
