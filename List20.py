'''
Python program to print all even numbers in a range

Input: start = 4, end = 15
Output: 4, 6, 8, 10, 12, 14

Input: start = 8, end = 11
Output: 8, 10

'''

start = int(input("Enter the start number:"))
end = int(input("Enter the end number:"))
for i in range(start,end+1):
    if i%2 == 0:
        print(i,end = " ")