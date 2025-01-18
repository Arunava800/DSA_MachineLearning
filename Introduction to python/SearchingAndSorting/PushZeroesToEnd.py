"""
You have been given a random integer array/list(ARR) of size N. You have been required to push
all the zeroes that are present in the array/list to the end of it. Also, make sure to maintain
the relative order of the non-zero elements
Parameters:
    N= size of the array
    arr = The given array
Input:
    N = 7
    array = [2, 0, 0, 1, 3, 0, 0]
Output:
[2, 3, 1, 0 , 0 , 0 0]

"""


def push_zeroes_to_end(arr, n):
    ptr = 0
    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
    print(arr)


N = int(input("Enter the number of terms: "))
array = list(map(int, input("Enter the elements present in the array").split()))
push_zeroes_to_end(array, N)
