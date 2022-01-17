from majwaeteul.judge import *

problem = Problem(1000)
problem.getRandomArray(100, 1, 100)
print(problem.getRandomArrayPair(5, 1, 5, 1, 5, True, order_type=1))

problem.Run()


