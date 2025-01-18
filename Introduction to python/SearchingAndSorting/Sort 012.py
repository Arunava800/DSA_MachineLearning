"""
You are given an integer array/list(ARR) of size N. It contains only 0s, 1s and 2s.
Write a solution to sort this array/list in a 'single scan'.
'Single Scan' refers to iterating over the array/list just once or to put it in other words,
you will be visiting each element in the array/list just once.
Input: [0, 1, 2, 0, 2, 0, 1]
Output: [0, 0, 0, 1, 1, 2, 2]
"""


def zero_one_two(arr, n):
    zeroes = 0
    twos = n - 1
    i = 0
    while i <= twos:
        if arr[i] == 0:
            arr[i], arr[zeroes] = arr[zeroes], arr[i]
            zeroes += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[twos] = arr[twos], arr[i]
            twos -= 1
