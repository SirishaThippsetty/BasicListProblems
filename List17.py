'''
Python program to find second largest number in a list

Input: list1 = [10, 20, 4]
Output: 10

Input: list2 = [70, 11, 20, 4, 100]
Output: 70



'''
list1 = [10, 20, 4]
list2 = [70, 11, 20, 4, 100]
list1.sort()
list2.sort()
print("The second largest in list1:",list1[-2])
print("The second largest in list2:",list2[-2])