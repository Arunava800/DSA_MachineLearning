"""
You have been given a random integer array/list(Arr) and a number X. Find and return the
number of triplets in the array/list which sums to x.
Input: 1
7
1 2 3 4 5 6 7
12
Output: 5
From the given list, the number of triplets that adds to 12 are:
(1,4,7),(1,5,6), (2,3,7),(2,4,6),(3,4,5),
"""


def find_triplet(arr: list, n: int, x: int) -> int:
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if arr[i]+arr[j]+arr[k] == x:
                    count += 1
    return count


n_terms = int(input("Enter the number of terms: "))
answer = 0
for terms in range(n_terms):
    target = int(input("Enter the target: "))
    array = list(map(int, input("Enter the elements in the the list").split()))
    answer = find_triplet(array, n_terms, target)
    print(answer)
