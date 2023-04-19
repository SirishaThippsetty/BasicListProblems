'''
Python | Ways to find length of list

'''
lst = [25,54,89,45,23,12,57,98,45,36]

# Method 1:
length = len(lst)
print("Length of the given list:",length)

# Method 2:
count = 0
for each in lst:
    count += 1
print("Length of the given list:",count)