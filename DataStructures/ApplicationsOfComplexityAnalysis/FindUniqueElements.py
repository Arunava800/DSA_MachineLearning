"""
You have been given an integer array/list(ARR) of size N. where N = [2M+1]. Now, in the given
list/array, `M` numbers are present twice and one number is present only once.
You need to find and return the number which is unique in the array/list.
Note:
    Unique element is always present according to the given condition.
"""


def find_unique(arr):
    unique = {}
    for i in arr:
        if i not in unique:
            unique[i] = unique.get(i, 1)
        else:
            unique[i] += 1
    for i in unique:
        if unique[i] == 1:
            return i


terms = int(input("Enter the number of elements: "))
array = list(map(int, input(f'Enter the {terms} in the array.').split()))
print(find_unique(array))
