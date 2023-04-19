'''
Remove multiple elements from a list in Python

Given a list of numbers, write a Python program to remove 
multiple elements from a list based on the given condition.

Input: [12, 15, 3, 10]
Output: Remove = [12, 3], New_List = [15, 10]

Input: [11, 5, 17, 18, 23, 50]
Output: Remove = [1:5], New_list = [11, 50]

''' 

'''
Example #1: Let’s say we want 
to delete each element in the list which is divisible by 2 or all the even numbers. 
'''
list1 = [11, 5, 17, 18, 23, 50] 
for each in list1:
    if each % 2 == 0:
        list1.remove(each)
print(list1)

'''
Removing all even elements in a list is as good as 
only including all the elements which are not even( i.e. odd elements).
'''

list2 = [11, 5, 17, 18, 23, 50] 
for each in list2:
    if each % 2 != 0:
        list2.remove(each)
print(list2)