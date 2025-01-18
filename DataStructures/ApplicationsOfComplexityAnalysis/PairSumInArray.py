"""
You have been given an integer array/list(ARR) and a number `num`. Find and return the total
number of pairs in the array/list which sum to `num`.
"""


def pair_sum(arr, n, num):
    arr.sort()
    start_index = 0
    end_index = n - 1
    num_pairs = 0
    while start_index < end_index:
        if arr[start_index] + arr[end_index] < num:
            start_index += 1
        elif arr[start_index] + arr[end_index] < num:
            end_index -= 1
        else:
            ele_start_index = arr[start_index]
            ele_end_index = arr[end_index]
            if ele_start_index == ele_end_index:
                ele_count = end_index + start_index + 1
                num_pairs += (ele_count * (ele_count - 1))//2
                return num_pairs
            temp_start_index = start_index + 1
            temp_end_index = end_index - 1
            while temp_start_index <= temp_end_index and arr[temp_start_index] == ele_start_index:
                temp_start_index += 1
            while temp_start_index <= temp_end_index and arr[temp_end_index] == ele_end_index:
                temp_end_index -= 1
            total_ele_start = temp_start_index - start_index
            total_ele_end = end_index - temp_end_index
            num_pairs += total_ele_start * total_ele_end
            start_index = temp_start_index
            end_index = temp_end_index
    return num_pairs


terms = int(input("Enter the number of terms: "))
array = list(map(int, input(f"Enter {terms} elements").split()))[:terms]
target = int(input("Enter the target of the sum"))
print(pair_sum(array, terms, target))