'''
Python program to select Random value from list of lists

Input : test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
Output : 7
Explanation : Random number extracted from Matrix.
'''
from itertools import chain
import random

test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
# choice() for random number, from_iterables for flattening
res = random.choice(list(chain.from_iterable(test_list)))
print(res)
