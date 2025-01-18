"""
Given a matrix size MxN, you must traverse the matrix row-wise. You must return an integer
array of size NxM denoting the row-wise traversal of the matrix.
Input: [[1,2,3],[4,5,6]]
Output: 1 2 3 4 5 6
"""


def print_row_wise(a):
    for rows in range (len(a)):
        for cols in range(len(a[i])):
            print(a[rows][cols], end=" ")


n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
matrix = []
for i in range(n):
    a = []
    for j in range(m):
        print(f"Enter the elements for {i} rows and {j} columns: ", end="")
        a.append(int(input()))
    matrix.append(a)
print_row_wise(matrix)