"""
A random integer array/list(ARR) of size N. Write a function to rotate the given array/list
by D elements.
Parameters:
    N = Size of the array
    arr = Array
    D = rotates the given array/list
Input:
terms = size of the array.
array = random array.
D = No of times the array is rotated
Example: [1 2 3 4 5 6 7]
Output: [3 4 5 6 7 1 2]
"""


def rotate(arr, n, d):
    """
    Method 1, this approach takes a lot more time
    """
    for i in range(d):
        temp = arr[0]
        j = 0
        while j < len(arr)-1:
            arr[j] = arr[j+1]
            j += 1
        arr[len(arr) - 1] = temp
        # j = 0
        # while j < len(arr)-1:
        #     arr[j], arr[j+1] = arr[j+1], arr[j]
        #     j += 1
    print(arr)


def rotate_first(arr, d):
    """
    This the second approach where the `d` elements are stored
    """
    temp = arr[:d]
    start = len(arr)-d
    for i in range(start):
        arr[i] = arr[i+d]
    for j in range(len(temp)):
        arr[start+j] = temp[j]
    print(arr)


def rotate_second(arr, d):
    arr = arr[::-1]
    f_part = arr[:len(arr)-d]
    f_part = f_part[::-1]
    s_part = arr[len(arr)-d:]
    s_part = s_part[::-1]
    arr = f_part + s_part
    print(arr)


def swap_elements(arr, start, end):
    arr[start], arr[end] = arr[end], arr[start]


def reverse(arr, start, end):
    while start < end:
        swap_elements(arr, start, end)
        start += 1
        end -= 1


def rotate_third(arr, n, d):
    if n == 0:
        return
    if d >= n != 0:
        d = d % n
    reverse(arr, 0, n - 1)
    reverse(arr, 0, n-d-1)
    reverse(arr, n-d, n-1)


terms = int(input("Enter the number of terms: "))
array = list(map(int, input("Enter the elements in the array: ").split()))[:terms]
r_times = int(input("Enter number of times the element is to be rotated: "))
# rotate(array, terms, r_times)
# rotate_first(array, r_times)
# rotate_second(array, r_times)
rotate_third(array, terms, r_times)
