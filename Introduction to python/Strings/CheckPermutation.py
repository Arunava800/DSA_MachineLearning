def check_permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    f_string = list(string1.lower())
    s_string = list(string2.lower())
    f_string.sort()
    s_string.sort()
    for i in range(len(f_string)):
        if f_string[i] != s_string[i]:
            return False
    return True


strng1 = input("Enter the first string: ")
strng2 = input("Enter the second string: ")
answer = check_permutation(strng1, strng2)
if answer:
    print("true")
else:
    print("false")

