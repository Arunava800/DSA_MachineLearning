from sys import stdin


def sumOfTwoArrays(arr1, n, arr2, m, output):
    # Your code goes here
    idx1, idx2, carry = n - 1, m - 1, 0
    idx3 = max(n, m)
    while idx1 >= 0 and idx2 >= 0:
        addition = arr1[idx1] + arr2[idx2] + carry
        tens, units = addition // 10, addition % 10
        output[idx3], carry = units, tens
        idx1 -= 1
        idx2 -= 1
        idx3 -= 1
    while idx1 >= 0:
        addition = arr1[idx1] + carry
        tens, units = addition // 10, addition % 10
        output[idx3], carry = units, tens
        idx1 -= 1
        idx3 -= 1
    while idx2 >= 0:
        addition = arr2[idx2] + carry
        tens, units = addition // 10, addition % 10
        output[idx3], carry = units, tens
        idx2 -= 1
        idx3 -= 1
    output[0] = carry


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    arr1, n = takeInput()
    arr2, m = takeInput()

    outputSize = (1 + max(n, m))
    output = outputSize * [0]

    sumOfTwoArrays(arr1, n, arr2, m, output)
    printList(output, outputSize)

    t -= 1