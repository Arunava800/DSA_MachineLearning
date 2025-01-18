"""
Populate the array using the integer values in the range 1 to N both inclusive in the order
[1,3,5,6,4,2] for the value N=6
Input: N, denotes the number of terms
Output: [1,3,5,6,4,2]
"""
n = int(input())  # number of terms
s_ptr = 0  # starting pointer
e_ptr = n - 1  # ending pointer
arr = [0] * n
flag = True
for i in range(1, n+1):
    if flag:
        arr[s_ptr] = i
        s_ptr += 1
        flag = False
    else:
        arr[e_ptr] = i
        e_ptr -= 1
        flag = True
print(arr)


