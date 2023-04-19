'''
Python - Swap elements in String list

Sometimes, while working with data records we can have a problem
 in which we need to perform certain swap operation in which we
need to change one element with other over entire string list. 
This has application in both day-day and data Science domain.
Lets discuss certain ways in which this task can be performed. 

'''
lst = ['Gfg','is','best','for','Geeks']
result = [i.replace('G','-').replace('e','G').replace('-','e') for i in lst]
print(result)