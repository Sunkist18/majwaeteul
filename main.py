from majwaeteul.judge import *

problem = Problem(1000)
problem.getRandomArray(100, 1, 100)
size = 10
print(problem.getRandomArrayPair(size, 1, 4, 1, 5, True, pair_type=1))
print(problem.getRandomArrayPair(size, 1, 4, 1, 5, False, pair_type=1))
problem.Run()
