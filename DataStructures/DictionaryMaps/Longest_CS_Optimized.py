"""
----------------------LONGEST CONSECUTIVE SEQUENCE-------------------------------------
You are given an unsorted array/list of `N` integers. Your task is to return the length of the
longest consecutive sequence.
The consecutive sequence is in the form ['NUM', 'NUM'+1, 'NUM'+2 ... 'NUM' + L], where
'NUM' is the starting integer of the sequence and 'L' + 1 is the length of the sequence.
Note: If there are any duplicates in the given array, we will count only one of them in the
consecutive sequence.
Sample Input: 1
              5
              [33,20,34,30,35]
Sample Output: 3--> [33, 34, 35]
"""


from typing import List


def consecutive_sequence(arr: List[int]) -> int:
    # stores the maximum of consecutive sequence
    max_element = 0
    sett = set()
    for element in arr:
        sett.add(element)
    for element in arr:
        previous_consecutive_element = element - 1
        if not (previous_consecutive_element in sett):
            j = element
            while j in sett:
                j += 1  # next consecutive element
            max_element = max(max_element, j - element)
    return max_element


array = list(map(int, input().split()))
print(consecutive_sequence(array))