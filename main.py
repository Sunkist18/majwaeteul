from pprint import pprint
from majwaeteul.co_judge import *

tc = TestCaseGenerator(1000)
pprint(tc.getRandomMatrix(10, 10, range(100), True))
print(tc.getRandomString(10, '1234567890', True))
