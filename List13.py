'''
Sum of number digits in List


The original list is : [12, 67, 98, 34]
List Integer Summation : [3, 13, 17, 7]

'''
lst = [12, 67, 98, 34]
sum_lst = []
for each in lst:
    total = 0
    for i in str(each):
        total += int(i)
    sum_lst.append(total)
    
   
print("List Integer Summation :",sum_lst) 