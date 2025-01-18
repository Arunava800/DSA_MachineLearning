"""
Given a matrix 'A' of size 'N'*'M', you must traverse the matrix column-wise. You must return
an integer array of size 'N'*'M' denoting column-wise traversal of the matrix.
Input: [[1,2,3],[4,5,6]]
Output: 1 4 2 5 3 6
"""


def print_column_wise(a):
    length = len(a)
    for cols in range(len(arr[0])):
        for rows in range(length):
            print(a[rows][cols],end=" ")




n = int(input("Enter the rows of the matrix: "))
m = int(input("Enter the columns of the matrix: "))
matrix = []
for i in range(n):
    arr = []
    for j in range(m):
        print(f"Enter the element at {i} row and {j} columns: ")
        arr.append(input())
    matrix.append(arr)
print_column_wise(matrix)
