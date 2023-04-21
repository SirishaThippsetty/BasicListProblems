'''
 Uncommon elements in Lists of List

'''
test_list1 = [ [1, 2], [3, 4], [5, 6] ]
test_list2 = [ [3, 4], [5, 7], [1, 2] ]
new = []
for each in test_list1:
   if each not in test_list2:
      new.append(each)
for each in test_list2:
   if each not in test_list1:
      new.append(each)
print(new)