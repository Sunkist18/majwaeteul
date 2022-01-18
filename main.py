from pprint import pprint
from majwaeteul.co_judge import *

tc = TestCaseGenerater(1000)
# test tc
# print(tc.getRandomArray(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(tc.getRandomArray(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True))
# print(tc.getRandomPairArray(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False, 1))
# print(tc.getRandomPairArray(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False, 2))
# print(tc.getRandomPairArray(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False, 3))
# print(tc.getRandomPairArray(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False, 4))
# print(tc.getRandomPairArray(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True, 1))
# print(tc.getRandomPairArray(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True, 2))
# print(tc.getRandomPairArray(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True, 3))
# print(tc.getRandomPairArray(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True, 4))
pprint(tc.getRandomMatrix(10, 5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
