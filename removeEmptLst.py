'''
Python – Remove empty List from List

test_list = [5, 6, [], 3, [], [], 9]

'''
test_list = [5, 6, [], 3, [], [], 9]
new_list = [i for i in test_list if i != []]
print(new_list)
