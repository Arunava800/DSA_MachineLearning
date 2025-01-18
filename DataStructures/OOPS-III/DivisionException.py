"""
Rishabh has recently learnt about the exception handling in Python.
Her teacher gave him a task to take two integers input from the user.
Now he wants to print the integral division of the integers. But there is a condition that
always he wants to print the last message as " Hey you are doing division". It means if
division is possible, so firstly he have to print the result of division and in the next line
 he have to print " Hey you are doing division" and if division is not possible, then he have
 to print "Division not possible" and in the next line he have to print " Hey you are doing
  division".
Help Rishabh in this task.
"""

a = int(input())
b = int(input())
try:
    res = a//b
    print(res)
except ZeroDivisionError:
    print("Division not possible")
print("Hey you are doing division")