'''
Python program to count Even and Odd numbers in a List

Input: list1 = [2, 7, 5, 64, 14]
Output: Even = 3, odd = 2

Input: list2 = [12, 14, 95, 3]
Output: Even = 2, odd = 2

'''
list1 = [2, 7, 5, 64, 14]
list2 = [12, 14, 95, 3]
even1,even2 = 0,0
odd1,odd2 = 0,0
for each in list1:
    if each % 2 == 0:
        even1 += 1
    else:
        odd1 += 1
for each in list2:
    if each % 2 == 0:
        even2 += 1
    else:
        odd2 += 1
print("Count of even numbers in List1:",even1,"Count of odd numbers in List1:",odd1)
print("Count of even numbers in List2:",even2,"Count of odd numbers in List2:",odd2)
