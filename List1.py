'''
Given a list, write a Python program to swap first and last element of the list.

Examples: 

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]

'''
given_list = [1,2,3]
length_list = len(given_list)
temp = given_list[0]
given_list[0] = given_list[-1]
given_list[-1] = temp
print(given_list)
