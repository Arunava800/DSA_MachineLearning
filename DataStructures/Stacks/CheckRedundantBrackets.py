"""
For a given expression in the form of a string, find if there exists any redundant brackets
or not. It is given that the expression contains only rounded brackets or parenthesis and the
input expression will always be balanced.
A pair of the bracket is said to be redundant when a sub-expression is surrounded by
unnecessary or needless brackets.
Example:
    Expression: (a+b)+c
    Since, there are no needless brackets, hence the output is false.
    Expression: ((a+b))
    The expression can be reduced to (a+b). Hence, the expression has redundant brackets and
    the output will be `true`
"""


# ------------UTILITY FUNCTIONS---------------------------- #

def find(ch):
    if ch == '+' or ch == '-' or ch == '*' or ch == '/':
        return True
    return False


def is_empty(stack):
    return len(stack) == 0


def top(stack):
    return stack[len(stack) - 1]
# ---------------------------------------------------------------------------------------#


def check_redundant_brackets(expression):
    stk = list()
    for i in range(len(expression)):
        if expression[i] == '(' or find(expression[i]):
            stk.append(expression[i])
        elif expression[i] == ')':
            has_operator = False
            while not is_empty(stk) and top(stk) != '(':
                stk.pop()
                has_operator = True
            if not has_operator:
                return True
            if not is_empty(stk):
                stk.pop()
    return False


input_string = input()
print(check_redundant_brackets(input_string))
