"""
Aadil has been provided with the sentence in the form of a string as a function parameter.
The task is to implement a function  to change the sentence such that each word in the
sentence is reversed. A word is a combination of characters without any space
"""


def reverse_word(new_string):
    n = ""
    for i in range(len(new_string)-1, -1, -1):
        n += new_string[i]
    return n+" "


def reverse_each_word(string):
    reversed_string = ""
    while True:
        space_index = string.find(" ")
        if space_index == -1:
            reversed_string += reverse_word(string)
            return reversed_string
        reversed_string += reverse_word(string[:space_index])
        string = string[space_index+1:]


strings = input("Enter a sentence")
ans = reverse_each_word(strings)
print(ans)
