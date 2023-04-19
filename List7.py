'''
Check if element exists in list in Python

The list is an important container in python as it stores elements of 
all the data types as a collection. Knowledge of certain list operations 
is necessary for day-day programming. This article discusses the Fastest way 
to check if a value exists in a list or not using Python.

Example:

list = test_list = [1, 6, 3, 5, 3, 4]
Input: 3  # Check if 3 exist or not.
Output: True
Input: 7  # Check if 7 exist or not.
Output: False


'''

test_list = [1, 6, 3, 5, 3, 4]
input_numb = int(input("Enter the number:"))
if input_numb in test_list:
    print("True")
else:
    print("False")