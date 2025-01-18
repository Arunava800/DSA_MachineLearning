"""
Given an integer N, count and return the number of zeros that are present in the
given integer using recursion.
Input: 0001024, 708000
Output: 1, 4
"""


def count_zeros(number: str, si, ei) -> int:
    if si > ei:
        return 0
    if number[si] == '0':
        ans = count_zeros(number, si+1, ei)
        if si == ei:
            return len(number)
        else:
            return ans
    else:
        ans = count_zeros(number, si, ei-1)
        if number[ei] == '0':
            return 1 + ans
        else:
            return ans


n = input("Enter the number: ")
print(count_zeros(n, 0, len(n)-1))


