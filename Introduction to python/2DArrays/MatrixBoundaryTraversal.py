"""
Given a matrix of integer 'M' rows and 'N' columns.  Print the boundary elements of the matrix.
The order of printing does not matter.
Input: M= 4, N = 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 1]
"""


def matrix_boundary_traversal(mat, m, n):
    b_array = []
    for row in range(m):
        for col in range(n):
            if row == 0 or col == 0 or row == m-1 or col == n-1:
                b_array.append(mat[row][col])
    return b_array


rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
matrix = []
for i in range(rows):
    a = []
    for j in range(columns):
        print(f"Enter the element in the {i} th row and the {j}th columns: ")
        a.append(int(input()))
    matrix.append(a)
ans = matrix_boundary_traversal(matrix, rows, columns)
print(ans)

