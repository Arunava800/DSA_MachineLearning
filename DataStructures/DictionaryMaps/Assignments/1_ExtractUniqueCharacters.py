"""
Given a string s, you need to remove all the duplicates. This means, the output string should
contain each character only once. The respective order of characters should remain same as
the input string.
SampleInput: ababacd
Sample Output: abcd
"""


def unique_char(word: str) -> str:
    characters = dict()
    string_list = ""
    for i in word:
        if word not in characters:
            characters[i] = characters.get(i, 1)

    for i in characters:
        string_list += i
    return string_list


s = input()
print(unique_char(s))