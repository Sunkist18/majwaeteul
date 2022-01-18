from pprint import pprint
from majwaeteul.co_judge import *

tc = TestCaseGenerator(1000)
pprint(tc.getRandomMatrix(10, 10, range(100), True))
print(tc.getRandomString(10, '1234567890', True))
print(tc.getUnweightedTree(10, 10, 1))
print(tc.getRandomCharMatrix(2, 2, '1234567890', True))
# check tree
print(tc.getUnweightedTree(10, 10, 1))
print(tc.getWeightedTree(10, 10, range(1, 15), 1))
