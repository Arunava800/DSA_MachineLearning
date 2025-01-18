"""
Given a string, where ever the word 'pi' is encountered, replace it with 3.14
Input: 'abcdpiedf'
Output: 'abcd3.14edf'
"""


def replace_pi(string):
    if len(string) == 0 or len(string) == 1:
        return string
    if string[0] == 'p' and string[1] == 'i':
        output = replace_pi(string[2:])
        return '3.14' + output
    else:
        output = replace_pi(string[1:])
        return string[0] + output


st = input("Enter the string: ")
print(replace_pi(st))
