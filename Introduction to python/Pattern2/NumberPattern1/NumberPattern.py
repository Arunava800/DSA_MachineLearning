times = int(input())
rows = 1
s_times = times
while rows <= times:
    # increasing pattern
    cols = 1
    while cols <= rows:
        print(cols, end="")
        cols += 1
    s_space = (2 * s_times) - 2
    while s_space > 0:
        print("", end=" ")
        s_space -= 1
    # decreasing pattern
    s_cols = rows
    while s_cols > 0:
        print(s_cols, end="")
        s_cols -= 1
    print()
    rows += 1
    s_times -= 1
