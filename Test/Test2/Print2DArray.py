def print_array(mat):
    length = len(mat)
    counter = 0
    n_rows = 0
    for x in range(length):
        while counter < length:
            rows = n_rows
            for cols in range(length):
                print(mat[rows][cols], end="")
            print()
            counter += 1
        n_rows += 1
        counter = n_rows

# n = int(input("Enter number of rows: "))
# m = int(input("Enter number of columns: "))
# matrix = []
# for i in range(n):
#     a = []
#     for j in range(m):
#         a.append(int(input()))
#     matrix.append(a)
# print_array(matrix)


li = list(map(int, input().split()))
mat = []
rows = li[0]
cols = li[1]
for i in range(rows):
    row = [int(ele) for ele in list(input().strip().split())]
    mat.append(row)


