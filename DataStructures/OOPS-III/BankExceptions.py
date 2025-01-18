class AccountLimitReached(Exception):
    def __init__(self, message:str, acc_no: str, amount:str) -> None:
        super().__init__(message)
        self.acc_no = acc_no
        self.amount = amount

    def print_error(self):
        message = super().__str__()
        print({
            'message': message,
            'account': self.acc_no,
            'amount': self.amount
        })


def withdraw_amount(acc_no: str, amount:str):
    raise AccountLimitReached("Reached account limit", acc_no, amount)

try:
    withdraw_amount('1000', '30000')
except AccountLimitReached as e:
    print(e)
    e.print_error()