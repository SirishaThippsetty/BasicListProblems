'''
Python program to print odd numbers in a List

Input: list1 = [2, 7, 5, 64, 14]
Output: [7, 5]

Input: list2 = [12, 14, 95, 3, 73]
Output: [95, 3, 73]

'''
list1 = [2, 7, 5, 64, 14]
list2 = [12, 14, 95, 3, 73]
odd_list1 = []
odd_list2 = []
for each in list1:
    if each % 2 != 0:
        odd_list1.append(each)
for each in list2:
    if each % 2 != 0:
        odd_list2.append(each)
print(odd_list1)
print(odd_list2)