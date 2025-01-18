"""
For a given string, find and return the highest occurring character.
Example:
    Input: `abcdeapapqarr
    Output: a
Since a has appeared four times in the string  which happens to be the highest frequency,
character, the answer would be `a`.
If there are two characters in the input string with same frequency, return the character
which comes first.
"""


def highest_occurring_character(string):
    char_array = [0] * 256
    max_value = -1
    temp = -1
    for i in string:
        ordinal_value = ord(i)
        char_array[ordinal_value] += 1
    for i in range(len(char_array)):
        if char_array[i] > max_value:
            max_value = char_array[i]
            temp = i
    return chr(temp)



strings = input("Enter the string: ")
ans = highest_occurring_character(strings)
print(ans)