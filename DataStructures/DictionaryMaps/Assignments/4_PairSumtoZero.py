"""
Given a random integer array `A` of size `N`, find and print the count pair of elements
in the array which sums up to zero.
Sample Input:
    5
    2 1 -2 2 3
Sample Output: 2--(2,-2) and (-2,2)
"""


from typing import List


def pair_sum(arr: List[int], n: int) -> int:
    pair_table = dict()
    count = 0
    for i in arr:
        if -i in pair_table:
            count += pair_table[-i]
        if i in pair_table:
            pair_table[i] += 1
        else:
            pair_table[i] = 1
    return count




elements = int(input("Enter the number of elements: "))
array = [int(x) for x in input().strip().split()]
print(pair_sum(array, elements))