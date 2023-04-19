'''
Python program to count positive and negative numbers in a list

Input: list1 = [2, -7, 5, -64, -14]
Output: pos = 2, neg = 3

Input: list2 = [-12, 14, 95, 3]
Output: pos = 3, neg = 1

'''
l1 = [2, -7, 5, -64, -14]
l2 = [-12, 14, 95, 3]
pos1,pos2 = 0, 0
neg1,neg2 = 0,0
for each in l1:
    if each>0:
        pos1 += 1
    else:
        neg1 += 1
for each in l2:
    if each>0:
        pos2 += 1
    else:
        neg2 += 1
print("Positive count in List1:",pos1)
print("Negative count in List1:",neg1)
print("Positive count in List2:",pos2)
print("Negative count in List2:",neg2)