"""
For a given two-dimensional array of size NxM, find and print the sum of each of the row
elements in a single line, separated by a single space.
Input: 4 2
1 2
3 4
5 6
7 8
Output: 3 7 11 15
"""


def row_wise_sum(matrices, n_rows, m_cols):
    for rows in range(n_rows):
        addition = 0
        for cols in range(m_cols):
            addition += matrices[rows][cols]
        print(addition, end=" ")


n = int(input("Enter the number of rows in the array: "))
m = int(input("Enter the number of columns in the array: "))
matrix = []
for i in range(n):
    a = []
    for j in range(m):
        print(f"Enter element in the {i} row and {j} columns: ")
        a.append(int(input()))
    matrix.append(a)

row_wise_sum(matrix, n, m)
