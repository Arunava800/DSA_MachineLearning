"""
Write a python program that defines two classes India and USA, each representing a country.
Both classes have methods to display information about the country's capital and language.
The program allows the user to choose between India and USA by entering the numbers(1 or 2)
and then it calls appropriate methods to display information about the selected country.
Requirements:
1. Create a python program that allows the user to input a number either 1 or 2 to select
between the countries: India and USA
2. Implement two classes: India and USA.
3. In the India class, implement a capital method that prints "New Delhi is the capital of
India" and a language method that prints "Hindi is most widely spoken language of India".
4. In the USA class, implement a capital method that prints "Washington, D.C. is the
capital of the USA" and the language method that prints  "English is the primary language of
the USA."
"""


class India:
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")


class USA(India):
    def capital(self):
        print("Washington, D.C. is the capital of  USA.")

    def language(self):
        print("English is the primary language of USA.")


choice = int(input())
if choice == 1:
    india = India()
    india.capital()
    india.language()
elif choice == 2:
    usa = USA()
    usa.capital()
    usa.language()
else:
    print("Invalid input. Please enter 1 for India or 2 for USA.")
