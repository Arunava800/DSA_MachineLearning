terms = int(input())
for rows in range(1, terms+1):
    for spaces in range(1, rows):
        print("", end=" ")
    for cols in range(rows, terms+1):
        print(cols, end="")
    print()
for rows in range(1, terms):
    for spaces in range(1, terms-rows):
        print("", end=" ")
    for cols in range(terms-rows, terms+1):
        print(cols, end="")
    print()
