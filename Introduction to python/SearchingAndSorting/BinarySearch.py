"""
Write a function to search `target` in the array`A`. If it exists, return its index in
0 - based indexing. If `target` is not present in the array `A`, return -1
Parameters:
    N = Size of the array
    A= Array
    Target = Element to be searched
Input: [1, 3, 7, 9, 11 12, 45], N= 7, Target = 3
Output: The index of element '3' is 1
Target = 10
The index of the element is -1
"""


def search(nums: [int], target: int) -> int:
    lower = 0
    upper = len(nums) - 1
    while lower <= upper:
        middle = (lower + upper) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            lower = middle + 1
        else:
            upper = middle - 1
    return -1


n = int(input("Enter the number of terms of the array: "))
arr = list(map(int, input(f"Enter {n} elements in the array: ").split()))[:n]
key = int(input("Enter the target value: "))
if search(arr,key) == -1:
    print("The target value is not present in the list")
else:
    print(f"The index value is {search(arr, key)}")
