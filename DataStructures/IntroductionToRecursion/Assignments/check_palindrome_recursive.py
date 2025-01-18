"""
Determine if a given string ‘S’ is a palindrome using recursion. Return a Boolean value
of true if it is a palindrome and false if it is not.

Note: You are not required to print anything, just implement the function. Example:
Input: s = "racecar"
Output: true
Explanation: "racecar" is a palindrome.
"""


def is_palindrome(string):
    if len(string) == 0:
        return ""
    answer = is_palindrome(string[1:])
    k = answer + string[0]
    return k


s = input("Enter the string: ")
print(is_palindrome(s))

