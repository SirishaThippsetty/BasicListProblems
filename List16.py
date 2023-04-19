'''
Python program to find largest number in a list

Input : list1 = [10, 20, 4]
Output : 20
Input : list2 = [20, 10, 20, 4, 100]
Output : 100

'''
list1 = [10, 20, 4]
list2 = [20, 10, 20, 4, 100]
large_list1 = max(list1)
large_list2 = max(list2)
print("Largest number in list1:",large_list1)
print("Largest number in list2:",large_list2)

list1.sort()
list2.sort()
print("Largest number in list1:",list1[-1])
print("Largest number in list2:",list2[-1])