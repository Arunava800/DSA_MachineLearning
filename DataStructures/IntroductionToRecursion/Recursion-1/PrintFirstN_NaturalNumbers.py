"""
Print the first N natural numbers using recursion
"""


def natural_n(n):
    if n == 0:
        return
    natural_n(n-1)
    print(n)


def natural_n_reverse(n):
    if n == 0:
        return
    print(n)
    natural_n_reverse(n-1)


number = int(input("Enter the range: "))
natural_n(number)
print("*"*20)
natural_n_reverse(number)