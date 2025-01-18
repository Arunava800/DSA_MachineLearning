def is_palindrome(number):
    remainder = 0
    reverse = 0
    while number > 0:
        remainder = number % 10
        reverse = reverse*10+remainder
        number = number // 10
    return reverse


n = int(input())
reverse_number = is_palindrome(n)
if n == reverse_number:
    print("true")
else:
    print("false")
