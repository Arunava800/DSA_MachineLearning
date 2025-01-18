"""
Given a list, find the sum of all the unique numbers
"""


def sum_unique(li):
    s = set()
    for i in li:
        s.add(i)
    sum_ = 0
    for i in s:
        sum_ += i
    return sum_


k = list(map(int, input("Enter the elements ").split(',')))
print(sum_unique(k))
