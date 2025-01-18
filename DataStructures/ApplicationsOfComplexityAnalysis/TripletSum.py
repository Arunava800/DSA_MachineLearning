"""
You have been given a random integer array/list(ARR) and a number x. Find and return the triplets
in the array/list which sum to x.
Sample Input:
7
1 2 3 4 5 6 7
12
Output: 5
"""


def triplet_sum(arr, n, target):
    arr.sort()
    ans = 0
    for i in range(n-2):
        low, high = i + 1, n - 1
        while low < high:
            curr_sum = arr[i] + arr[low] + arr[high]
            if curr_sum == target:
                ans += 1
                tmp_high = high - 1
                while tmp_high > low:
                    if arr[high] == arr[tmp_high]:
                        ans += 1
                        tmp_high -= 1
                    else:
                        break
                low += 1
            elif curr_sum > target:
                high -= 1
            else:
                low += 1
    return ans


terms = int(input("Enter the number of elements of the array"))
array = list(map(int, input(f"Please enter {terms} elements").split()))[:terms]
t = int(input("Enter the target element"))
print(triplet_sum(array, terms, t))
