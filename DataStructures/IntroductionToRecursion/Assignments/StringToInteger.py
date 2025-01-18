"""
Write a recursive function to convert a given string into the number it represents. That is
input will be numeric string that contains only numbers, you need to convert the string into
corresponding integer and return the answer.
"""


def string_to_number(string: str) -> int:
    length = len(string)
    if length == 0:
        return 0
    string_to_number(string[:-1])
    k = int(string)
    return k


s = input("Enter the number: ")
print(string_to_number(s))
