'''
Python program to print all odd numbers in a range

Input: start = 4, end = 15
Output: 5, 7, 9, 11, 13, 15

Input: start = 3, end = 11
Output: 3, 5, 7, 9, 11

'''

start = int(input("Enter the start number:"))
end = int(input("Enter the end number:"))
for i in range(start,end+1):
    if i%2 != 0:
        print(i,end = " ")

