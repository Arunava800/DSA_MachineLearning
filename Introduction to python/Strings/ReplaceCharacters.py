"""
You have been given a string. Replace every character of the string with the given character.
Input: abcda
Ouput: ebcde
"""


def replace(str, char1, char2):
    new_str = ""
    for char in str:
        if char == char1:
            new_str += char2
        else:
            new_str += char
    return new_str


string = input("Enter a string: ")
charac1 = input("Enter the character to be replaced: ")
charac2 = input("Enter the new character: ")
ans = replace(string, charac1, charac2)
print(ans)