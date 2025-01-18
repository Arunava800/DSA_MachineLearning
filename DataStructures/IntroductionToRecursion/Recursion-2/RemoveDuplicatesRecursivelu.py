"""
Given a string s, remove consecutive duplicates from it recursively.
Input: aaabbccc
Output: abc
"""


def remove_consecutive_duplicates(string):
    if len(string) == 0 or len(string) == 1:
        return string
    answer = remove_consecutive_duplicates(string[1:])
    if string[0] == string[1]:
        return "" + answer
    else:
        return string[0] + answer


s = input("Enter the string: ")
print(remove_consecutive_duplicates(s))
