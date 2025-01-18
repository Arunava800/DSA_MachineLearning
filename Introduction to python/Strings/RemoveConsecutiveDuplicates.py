"""
For a given string (str), remove all the consecutive duplicates characters.
Input: `aabbccc`
Output: abc
"""


def remove_duplicates(string):
    i = 0
    length = len(string)
    string_list = list(string)
    while i < length - 1:
        if string_list[i] == string_list[i+1]:
            string_list.pop(i)
            length = len(string_list)
            i = 0
        else:
            i += 1
    return ''.join(string_list)


strings = input("Enter the string: ")
ans = remove_duplicates(strings)
print(ans)
