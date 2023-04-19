'''
Find sum and average of List in Python

Input: [4, 5, 1, 2, 9, 7, 10, 8]
Output:
sum =  46
average =  5.75

'''

lst = [4, 5, 1, 2, 9, 7, 10, 8]
sum_lst = sum(lst)
avg_lst = sum_lst/len(lst)
print("Sum of the given list:",sum_lst)
print("Average of the given list:",round(avg_lst,2))