"""
For a given two-dimensional integer array/list of size (NxM), you need to find out which row or
column has the largest sum( sum of all elements in a row or column) amongst all the row/columns.
Note:
    If there are more than one rows/columns with maximum sum, consider the row/columns that comes
    first. And if ith row and jth column has the same largest sum, consider the ith row as the
    answer.
Input:
1
3 2
6 9
8 5
9 2
Output:
column 0 23
"""


import math
def maximum_row(mat, n_row, m_col):
    maximum = -2147483648
    temp = 0
    for row in range(n_row):
        addition = 0
        for col in range(m_col):
            addition += mat[row][col]
            if maximum < addition:
                maximum = addition
                temp = row
    return maximum, temp


def maximum_columns(mat, n_row, m_col):
    maximum = -2147483648
    temp = 0
    for cols in range(m_col):
        addition = 0
        for row in range(n_row):
            addition += mat[row][cols]
            if maximum < addition:
                maximum = addition
                temp = cols
    return maximum, temp


def find_largest_number(arr, n_rows, m_cols):
    max_row, rows = maximum_row(arr, n_rows, m_cols)
    max_cols, cols = maximum_columns(arr, n_rows, m_cols)
    if max_row > max_cols:
        return "row", rows, max_row
    elif max_cols > max_row:
        return "columns", cols, max_cols
    else:
        return "row", rows, max_row


n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
matrix = []
for i in range(n):
    a = []
    for j in range(m):
        print(f"Enter the {i} row and {j} column: ")
        a.append(int(input()))
    matrix.append(a)
printed, max_index, max_sum = find_largest_number(matrix, n, m)
print(printed, max_index, max_sum)