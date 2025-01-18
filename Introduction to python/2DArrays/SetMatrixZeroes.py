"""
Given a matrix 'N'x'M', if an element is 0, set its entire row and column to 0s, and return
the matrix. In particular, your task is to modify it in such a way that if a cell has a value 0
that is matrix[i][j] = 0, then all elements of its ith row and jth column should be changed to 0.
You must do it in place.
Input:[[7,9,13],[4,21,0]]
Output: [[7, 19, 0], [0,0,0]]
"""


def set_matrix_zero(mat):
    first_row = False
    first_column = False
    n = len(mat)
    m = len(mat)
    for i in range(n):
        if mat[0][0] == 0:
            first_column = True
            break
    for i in range(m):
        if mat[0][i] == 0:
            first_row = True
            break
    for i in range(1,n):
        for j in range(1, m):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][i] = 0
    for i in range(1, n):
        for j in range(1, m):
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0
    if first_column:
        for i in range(n):
            mat[i][0] = 0
    if first_row:
        for i in range(m):
            mat[0][i] = 0
    return mat


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of cols: "))
matrix = []
for k in range(rows):
    a = []
    for o in range(cols):
        print(f"Enter elements in the {k}th row and the {o}th column:")
        a.append(int(input()))
    matrix.append(a)

ans = set_matrix_zero(matrix)
print(ans)