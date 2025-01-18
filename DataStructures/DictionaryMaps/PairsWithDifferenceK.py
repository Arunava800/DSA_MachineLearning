"""
You are given with an array of integers and an integer `k`. You have to find and print
the count  of all such pairs which have difference `k`
Note: take absolute difference between the elements of the array.

Sample Input:
    4
    5 1 2 4
    3
Sample Output: 2
Explanation (5,2) and (1,4) are the possible combinations as their absolute difference is three

"""


def print_pair_difference_k(arr, target):
    pair_count = 0
    m = {}
    for num in arr:
        if num + target in m:
            pair_count += m[num + target]
        if target != 0 and num - target in m:
            pair_count += m[num - target]
        if num in m:
            m[num] += 1
        else:
            m[num] = 1
    return pair_count

        
elements = int(input("Enter the number of elements: "))
k = int(input("Enter the target: "))
array = [int(x) for x in input().split()]
count_difference = print_pair_difference_k(array, k)
print(count_difference)
