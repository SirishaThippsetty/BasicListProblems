'''
Python program to print even numbers in a list

Input: list1 = [2, 7, 5, 64, 14]
Output: [2, 64, 14]
Input: list2 = [12, 14, 95, 3]
Output: [12, 14]

'''

list1 = [2, 7, 5, 64, 14]
list2 = [12, 14, 95, 3]
even_list1 = []
even_list2 = []
for each in list1:
    if each % 2 == 0:
        even_list1.append(each)
for each in list2:
    if each % 2 == 0:
        even_list2.append(each)
print(even_list1)
print(even_list2)