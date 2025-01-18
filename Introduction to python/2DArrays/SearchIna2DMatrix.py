"""
You have been given a 2-D array 'MAT' of size MxN where 'M' and 'N' denotes the number of rows
and columns, respectively. The elements of each row are sorted in a non-decreasing order.
Moreover, the first element of a row is greater than the last element of the previous row
(if exists). You are given an integer target, and your task is to find out if it exists in the
'MAT' or not.
Example: Given Matrix: 1 1 and Target: 8
4 8
Output: True
"""


def find_target_in_matrix(mat, n_rows, m_cols, target):
    for rows in range(n_rows):
        for cols in range(m_cols):
            if mat[rows][cols] == target:
                return True
            elif mat[rows][cols] > target:
                return False
    return False


n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
matrix = []
for i in range(n):
    a = []
    for j in range(m):
        a.append(int(input()))
    matrix.append(a)
t = int(input("Enter the target: "))
ans = find_target_in_matrix(matrix, n, m, t)
if ans:
    print("TRUE")
else:
    print("FALSE")
