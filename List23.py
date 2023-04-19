'''
Python program to print positive numbers in a list

Input: list1 = [12, -7, 5, 64, -14]
Output: 12, 5, 64

Input: list2 = [12, 14, -95, 3]
Output: [12, 14, 3]

'''
l1 = [12, -7, 5, 64, -14]
l2 = [12, 14, -95, 3]
op1 = []
op2 = []
for each in l1:
    if each > 0:
        op1.append(each)
for each in l2:
    if each > 0:
        op2.append(each)
print(op1)
print(op2)