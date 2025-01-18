"""
For a given expression in the form of a string, find teh minimum number of brackets that
can be reversed in order to make an expression balanced. The expression contains only curly
brackets. If the expression can't be balanced, return -1
Example: {{{{
If we reverse second and fourth opening brackets, the whole expression gets balanced. Since,
we have to reverse two brackets to make the expression balanced, the expected output will be
2.
Example: {{{
In this example, if we reverse the last opening bracket, we would be left with first opening
bracket and we will not be able to make the expression balanced, and the output will be -1.
"""


def count_bracket_reversal(string):
    if len(string) == 0:
        return -1
    if len(string) % 2 != 0:
        return -1
    s = list()
    for char in string:
        if char == "{":
            s.append(char)
        else:
            if len(s) > 0 and s[-1] == "{":
                s.pop()
            else:
                s.append(char)
    count = 0
    while len(s) != 0:
        c1 = s.pop()
        c2 = s.pop()
        if c1 != c2:
            count += 2
        else:
            count += 1
    return count


string = input()
ans = count_bracket_reversal(string)
print(ans)