'''
Minimum of two numbers in Python

Given two numbers, write a Python code to find the Minimum of these two numbers. Examples:

Input: a = 2, b = 4
Output: 2

Input: a = -1, b = -4
Output: -4

'''


a = int(input("Enter the number 1:"))
b = int(input("Enter the number 2:"))

minimum = min(a,b)
print("Minimum of the given two numbers:",minimum)