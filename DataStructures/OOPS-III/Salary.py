"""
Rishabh has recently learnt about custom exceptions. His friend gave him  a task to initialise
the salary with 500 in a class and raise an exception with message as 'Insufficient funds in the
account; if the withdrawal amount is greater than the bank balance otherwise display a message
as 'Remaining: remaining balance'.
"""


class BalanceExceeded(Exception):
    def __init__(self, message):
        super().__init__(message)


def withdraw_amount(data):
    amount = 500
    net_amount = amount - data
    if net_amount <= 0:
        raise BalanceExceeded('Insufficient funds in the account')
    else:
        print('Remaining:', net_amount)


try:
    withdraw_amount(1000)
except BalanceExceeded as e:
    print(e)
