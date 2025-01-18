"""
You have been given an integer array/list(ARR) of size N which contains number from 0 to N-2.
Each number is present at least once. That is, if N=5,  the array/list constitutes values
ranging from 0 to 3, and among these, there is a single integer value that is present twice.
You need to find and return that duplicate number present in the array.
Note:
    Duplicate number is always present in the given array/list.
Sample Input:
    1
    9
    0 7 2 5 4 7 1 3 6
Sample Output:
7
"""


def find_duplicate(arr, n):
    sum_first_n_nums = ((n-2) * (n-1))/2
    sum_elements = 0
    for i in range(n):
        sum_elements += arr[i]
    return int(sum_elements - sum_first_n_nums)


terms = int(input("Enter the number of elements present in the array: "))
array = list(map(int, input(f"Enter the {terms} in the array").split()))
print(find_duplicate(array, terms))