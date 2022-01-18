from pprint import pprint
from majwaeteul.co_judge import *

tc = TestCaseGenerator(1000)
# check tree
print(sorted(tc.getRandomWeightedTree(8, 0)))
