"""
You have been given two integer array/list (Arr1, Arr2) of size `N` and `M`, respectively.
You need to print their intersection; An intersection for this problem can be defined when both
the arrays/lists contain a particular value or to put it in other words, when there is a
common value that exists in both arrays or lists.
Note:
    Input arrays/ lists can contain duplicate elements. The intersection elements printed .
"""

from typing import List


def print_intersection(arr1: List[int], n1: int, arr2: List[int], n2: int) -> None:
    elements_dictionary = dict()
    for i in arr1:
        if i not in elements_dictionary:
            elements_dictionary[i] = elements_dictionary.get(i, 1)
        else:
            elements_dictionary[i] += 1
    for i in arr2:
        if i in elements_dictionary:
            print(i)
            elements_dictionary[i] -= 1
            if elements_dictionary[i] == 0:
                elements_dictionary.pop(i)


n_elements = int(input("Enter the elements in the first list"))
m_elements = int(input("Enter the elements in the second list"))
array1 = [int(x) for x in input().strip().split()][:n_elements]
array2 = [int(x) for x in input().strip().split()][:m_elements]
print_intersection(array1, n_elements, array2, m_elements)
