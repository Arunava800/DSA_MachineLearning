"""
A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps
at a time. Implement a method, to count how many possible ways the child can run up to the stairs
You need to return number of possible ways W.
Input:4, 5
Output: 7, 13
"""


def stair_case(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return stair_case(n-1) + stair_case(n-2) + stair_case(n-3)


steps = int(input("Enter the input: "))
print(stair_case(steps))