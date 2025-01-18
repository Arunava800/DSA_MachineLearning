"""
Your task is to implement the divide function and demonstrate its functionality by creating a
python program.
Description:
1. If y is zero, the function should raise a ZeroDivisionError and print the message
'Sorry! You are dividing by zero.' If y is not zero, the function should return the result of
dividing x by y.
2. Implement a try-except block to handle the ZeroDivisionError exception within the divide
function.
3. Call the divide function with the provided values and print the result if successful,
or the error message if a ZeroDivisionError occurs.
4. Ensure that the finally block in the divide function is used to print the message
'This is always executed' regardless of whether an exception is raised or not.

"""


x = int(input())
y = int(input())


def divide(a, b):
    try:
        res = a/b
        print(res)
    except ZeroDivisionError:
        print('Sorry! You are dividing by zero')
    finally:
        print('This is always executed')


divide(x,y)
