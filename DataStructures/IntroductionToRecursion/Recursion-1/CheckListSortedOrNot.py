"""
List is sorted or not
"""


def is_sorted(a):
    length = len(a)
    if length == 0 or length == 1:
        return True
    if a[0] > a[1]:
        return False
    smaller_list = a[1:]
    is_smaller_sorted = is_sorted(smaller_list)
    if is_smaller_sorted:
        return True
    else:
        return False


a = [10, 2, 3, 5]
print(is_sorted(a))