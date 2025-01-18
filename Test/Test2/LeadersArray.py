def leaders_array(arr):
    stack_pos = 0
    inc_pos = stack_pos + 1
    while stack_pos < len(arr):
        if stack_pos == len(arr) - 1:
            print(arr[stack_pos])
            stack_pos  += 1
        elif arr[stack_pos] < arr[inc_pos]:
            stack_pos += 1
        elif inc_pos == len(arr) - 1:
            print(arr[stack_pos], end=" ")
            stack_pos = stack_pos + 1
            inc_pos = stack_pos + 1
        else:
            inc_pos += 1

number = int(input("Enter the number of elements present in the array: "))
array = list(map(int, input("Enter the elements present in the array: ").split()))
leaders_array(array)