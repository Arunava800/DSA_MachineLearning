"""
For a given two-dimensional integer array/list of size NxM, print the array/list in the
sine wave order ( that is, print the first column top to bottom, next column bottom to top
and so on).

Input:
1
3 4
1 2 3 4
5 6 7 8
9 10 11 12
Output:
1 5 9 10 6 2 3 7 11 12 8 4
"""


def print_sine_wave(matrix, n, m):
    ans = []
    for cols in range(m):
        if cols % 2 == 0:
            for row in range(0,n):
                ans.append(matrix[row][cols])
        else:
            for row in range(n-1, -1, -1):
                ans.append(matrix[row][cols])
    print(ans)


print_sine_wave([[1, 2, 3],[4, 5, 6], [7, 8, 9]], 3, 3)