"""
Given an array consisting of positive and negative integers, find the length of the longest
subarray whose sum is zero.
Sample Input:
10
95 -97 -387 -435 -5 -70 897 127 23 284
Sample Output: 5
Explanation: The five elements that form the longest subarray that sum up to zero are:
-387 -435 -70 897
"""

from typing import List


def subset_sum(list_elements: List[int]) -> int:
    length = len(list_elements)
    sum_values = [0] * length
    sum_values[0] = list_elements[0]
    start, end= -1, -2
    element_dict = {list_elements[0]: 0}
    if sum_values[0] == 0:
        start, end = 0, 0
    for i in range(1, length):
        sum_values[i] = sum_values[i-1] + list_elements[i]
        if sum_values[i] == 0:
            start, end = 0, i
        elif sum_values[i] in element_dict:
            if i - element_dict[sum_values[i]] > end - start + 1:
                start, end = element_dict[sum_values[i]], i
        else:
            element_dict[i] = i
    return end - start + 1

n = int(input())
elements = list(int(x) for x in input().strip().split())
print(subset_sum(elements))
