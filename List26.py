'''
Python program to print all negative numbers in a range

Input: a = -4, b = 5
Output: -4, -3, -2, -1

Input: a = -3, b= 4
Output: -3, -2, -1

'''
start = int(input("Enter the start number:"))
end = int(input("Enter the end number:"))
for i in range(start,end+1):
    if i < 0:
        print(i,end = " ")