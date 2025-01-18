terms = int(input())
row_1 = terms//2
row_2 = row_1 + 1
for rows in range(1, row_2+1):
    for spaces in range(1, row_2-rows+1):
        print("", end=" ")
    for cols in range(1, rows*2):
        print("*", end="")
    print()
for rows in range(row_1, 0, -1):
    for spaces in range(1, row_2-rows+1):
        print("", end=" ")
    for cols in range(1, 2*rows):
        print("*", end="")
    print()
