"""
You are given a square matrix of non-negative integers 'MATRIX'. Your task is to rotate
that array by 90 degrees in an anti-clockwise direction using constant space.
For example:
For given 2D array:
[[1, 2, 3],[4, 5, 6], [7, 8, 9]] after 90 degrees rotation in anti-clockwise direction, it will
become [[3, 6, 9],[2, 5, 8], [1, 4, 7]]
"""


def rotate_matrix(mat):
    for row in range(len(mat)):
        for col in range(len(mat)):
            if row < col:
                mat[row][col], mat[col][row] = mat[col][row], mat[row][col]

    ptr_a, ptr_b = 0, len(mat)-1
    while ptr_a < ptr_b:
        mat[ptr_a], mat[ptr_b] = mat[ptr_b], mat[ptr_a]
        ptr_a += 1
        ptr_b -= 1
    return mat


n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
matrix = []
for i in range(n):
    a = []
    for j in range(m):
        print(f"Enter the {i} and the {j} columns: ")
        a.append(int(input()))
    matrix.append(a)
print(rotate_matrix(matrix))