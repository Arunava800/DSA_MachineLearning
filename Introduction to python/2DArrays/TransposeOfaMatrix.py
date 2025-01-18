"""
You are given a matrix 'MAT'. print and return the transpose of the matrix. The transpose
of a matrix is obtained by changing the rows to columns and columns to rows. In other words,
transpose of a matrix A[][] is obtained by changing A[i][j] to A[j][i].
Input:
1 2
3 4
Output:
1 3
2 4
"""


def matrix_transpose(mat, n_row, m_col):
    new_matrix = []
    for col in range(m_col):
        x = []
        for row in range(n_row):
            x.append(mat[row][col])
        new_matrix.append(x)
    print(new_matrix)


n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
matrix = []
for i in range(n):
    a = []
    for j in range(m):
        print(f"Enter the {i} row and {j} cols: ")
        a.append(int(input()))
    matrix.append(a)
matrix_transpose(matrix, n, m)
