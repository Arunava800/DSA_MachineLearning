"""
Given an array of integers denoted by `A`, and let another `k` is provided. Determine
how many distinct integers are present in the list, such that they add to the value of `k`.
Sample Input: [2 1 3 4 2 3 5 6 1 2]
sample output: 7
"""


def pair_sum(arr, target):
    ans = 0
    freq = dict()
    for num in arr:
        expected = target - num
        ans += freq.get(expected, 0)
        if freq.get(num, 0):
            freq[num] += 1
        else:
            freq[num] = 1
    return ans


array = [int(x) for x in input().split()]
k = int(input("Enter the target"))
count = pair_sum(array, k)
print(count)