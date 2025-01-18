"""
For a given string (str) and a character x, write a function to remove all  the
occurrences of x from the given string.
"""


def remove_all_occurrences_of_char(string, ch):
    if ch in string:
        while True:
            index = string.find(ch)
            if index == -1:
                return string
            else:
                string = string[:index] + string[index + 1:]
    else:
        return string


strings = input("Enter the string: ")
char = input("Enter the character to be removed: ")
ans = remove_all_occurrences_of_char(strings, char)
print(ans)
