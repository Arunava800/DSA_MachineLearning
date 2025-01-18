"""
Given a string `S`, compute recursively a new string where identical chars that are adjacent
in the original string are separated from each other by a `*`.
"""


def print_star(string):
    if len(string) == 1:
        return string
    answer = print_star(string[1:])
    if string[0] == string[1]:
        output = string[0] + "*" + answer
    else:
        output = string[0] + answer
    return output


s = input("Enter the string")
print(print_star(s))