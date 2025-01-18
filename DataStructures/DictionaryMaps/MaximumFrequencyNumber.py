"""
You are given an array of integers that contains numbers in random order. Write a program to find
and return the number which occurs the maximum times in the given input.
If two or more elements are having maximum frequency,  return the element which occurs in the
array list first.
"""


def maximum(arr):
    d = dict()
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = d.get(i, 0)
    ans = 0
    for num in arr:
        if d[num] > d[ans]:
            ans = num
    return ans


element = int(input("Enter the number of elements"))
array_list = [int(x) for x in input().split()][:element]
max_occurring = maximum(array_list)
print(max_occurring)