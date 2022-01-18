from pprint import pprint
from majwaeteul.co_judge import *

tc = TestCaseGenerater(1000)
pprint(tc.getRandomMatrix(10, 10, range(100), True))
