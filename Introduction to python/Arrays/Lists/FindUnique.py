"""
Find and return the number which is  unique in the array list.
Parameters:
    N= Size of the array which is equal to [2M+1]
    M= Number of elements that are present twice
Input:
 array which has only one input element. Example: [2 3 1 6 3 6 2]
 Output: Unique element present in the array. Example: 1
"""


def find_unique(arr: list, n: int) -> int:
    i = 0
    while i < len(arr):
        if i == 0:
            if arr[i] not in arr[i+1:]:
                return arr[i]
        elif 0 < i < len(arr)-1:
            if arr[i] not in arr[:i] and arr[i] not in arr[i+1:]:
                return arr[i]
        if i == len(arr)-1:
            if arr[i] not in arr[:i]:
                return arr[i]
        i += 1


terms = int(input("Enter the number of terms: "))
array = [int(i) for i in input("Enter the array elements").split()]
answer = find_unique(array, terms)
print(answer)