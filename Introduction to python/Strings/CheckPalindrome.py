"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters.
Parameters:
    strings: Input the string
Input: malayalam
Output True
"""


def check_palindrome(string):
    reverse_string = string[::-1].lower()
    return reverse_string


input_ = input("Enter the string: ")
answer = check_palindrome(input_)
if input_.lower() == answer:
    print("true")
else:
    print("false")
