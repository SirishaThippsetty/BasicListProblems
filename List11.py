'''
Python | Count occurrences of an element in a list

Given a list in Python and a number x,
count the number of occurrences of x in the given list.

Examples: 

Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10], x = 10
Output: 3 
Explanation: 10 appears three times in given list.

Input: lst = [8, 6, 8, 10, 8, 20, 10, 8, 8], x = 16
Output: 0
Explanation: 16 appears zero times in given list.

'''

lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
ip_number = int(input("Enter the number:"))
appear_count = lst.count(ip_number)
print(appear_count)