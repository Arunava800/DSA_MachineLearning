"""
Given a string, replace all the occurrences of string1 with string2.
Input: There is a big cat, 'a', 'b'
Output: There is b big cbt
"""


def replace_string(string, string1, string2):
    length = len(string)
    if length == 0:
        return string
    answer = replace_string(string[1:], string1, string2)
    if string[0] == string1:
        return string2 + answer
    else:
        return string[0] + answer


m_string = input("Enter the string: ")
f_char = input("Enter the character: ")
s_char = input("Enter the second character: ")
print(replace_string(m_string, f_char, s_char))
