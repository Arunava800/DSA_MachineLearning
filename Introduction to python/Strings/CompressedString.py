"""
Write a program to do a basic string compression. For a character which is consecutively repeated
more than once, replace consecutive duplicate occurrences with the count of repetitions.
Example: If the string has 'x' repeated 5 times, replace this 'xxxxx' with 'x5'.
Consecutive count of every character in the input string is less than or equal to 9.
"""


def compressed_string_(s) -> str:
    ans = ""
    currChar = s[0]
    currLen = 1
    for i in range(1, len(s)):
        if s[i] == currChar:
            currLen += 1
        else:
            ans += currChar
            if currLen != 1:
                ans += str(currLen)
            currChar, currLen = s[i], 1
    ans += currChar
    if currLen != 1:
        ans += str(currLen)
    return ans

string = input("Enter the string: ")
ans = compressed_string_(string)
print(ans)


