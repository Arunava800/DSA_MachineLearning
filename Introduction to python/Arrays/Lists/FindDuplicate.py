"""
Find and return the duplicate number present in the array
Input: N -> Elements from 0 to N-2
        Example: N=9, list ranges from 0 to 7
        [0 7 2 5 4 7 1 3 6]
Output: The duplicate element
        7
"""


def duplicate_number(arr: list, n: int) -> int:
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]
    return -1


terms = int(input("Enter the number of elements"))
array = list(map(int, input("Enter the elements in the list").split()))
answer = duplicate_number(array, terms)
print(answer)
