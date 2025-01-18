"""
Given a string, compute recursively a new string where 'x' chars have been removed
Input: xaxb
output: ab
"""


def remove_x(string, char):
    if len(string) == 0:
        return string
    answer = remove_x(string[1:], char)
    if string[0] != char:
        return string[0] + answer
    else:
        return "" + answer


m_string = input("Enter the string: ")
x = input("Enter the character to be removed: ")
print(remove_x(m_string, x))