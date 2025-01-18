"""
Suppose you have a string S, made up of only a's and b's. Write a recursive function that
checks if the string was generated using the following rules:
a. The string begins with an 'a'.
b. Each 'a' is followed by nothing or an 'a' or 'bb'
c. Each 'bb' is followed by nothing or an 'a'.
"""


def helper(s):
    if len(s) == 0:
        return True
    if s[0] == 'a':
        if len(s[1:]) > 1 and s[1:3] == 'bb':
            return helper(s[3:])
        else:
            return helper(s[1:])
    else:
        return False


def check_ab(s):
    if s[0] != 'a':
        return False
    return helper(s)


string = input("Enter the string: ")
print(check_ab(string))
