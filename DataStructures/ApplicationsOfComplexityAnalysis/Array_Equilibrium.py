"""
For a given array/list of size `N` find and return the equilibrium index of the array/list.
Equilibrium index of a list/array is an index `i` such that the sum of the elements at indices
0 to i-1 is equal to the sum of the elements at indices `(i+1)`  to `(n-1)`. One thing to note
here is, the item at index `i` is not included in either part. If more than one equilibrium index
are present, then the index appearing first, in left to right fashion should be returned. Negative
-1, if no such index is present.
"""


def array_equilibrium_index(arr, n):
    tot_sum = 0
    for i in range(n):
        tot_sum += arr[i]
    left_sum = 0
    curr_index = 0
    while curr_index < n:
        right_sum = tot_sum - left_sum - arr[curr_index]
        if right_sum == left_sum:
            return curr_index
        left_sum = left_sum + arr[curr_index]
        curr_index += 1
    return -1


terms = int(input("Enter the number of elements: "))
array = list(map(int, input(f"Enter the {terms} elements: ").split()))[:terms]
print(array_equilibrium_index(array, terms))