"""
Given a string, print all the words with frequency k.
Input: this is a word string having many many words.
    2
Output: many
"""


def print_k_frequency_words(s, k):
    words = s.split()
    d = {}
    for w in words:
        d[w] = d.get(w, 0) + 1
    for w in d:
        if d[w] == k:
            print(w)


word = input("Enter the word: ")
freq = int(input("Enter the frequency: "))
print_k_frequency_words(word, freq)
