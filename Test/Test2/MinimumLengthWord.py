def minimum_length(string):
    list_string = string.split()
    index = 0
    minimum = len(list_string[0])
    for i in range(len(list_string)):
        length = len(list_string[i])
        if length < minimum and length != minimum:
            minimum = length
            index = i
    return list_string[index]


s = input("Enter the string: ")
print(minimum_length(s))
