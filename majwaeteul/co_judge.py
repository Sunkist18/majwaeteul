import random


class TestCaseGenerater:
    def __init__(self, problem_id: int):
        self.problem_id = problem_id

    def getRandomNumber(self, values: list) -> int:
        """Retrun a random number from the list
        Args:
            values (list): List of values
        Returns:
            int: Random number
        """
        return random.choice(values)

    def getRandomArray(self, size: int, values: list, distinct: bool = False) -> list:
        """Return a random array
        Args:
            size (int): Size of the array
            values (list): List of values
            distinct (bool, optional): If True, the array will be distinct. Defaults to False.
        Returns:
            list: Random array
        """
        if distinct:
            return random.sample(values, size)
        else:
            return [self.getRandomNumber(values) for _ in range(size)]

    def getRandomPairArray(self, size: int, x_values: list, y_values: list, pair_distinct: bool = True, order=0) -> list:
        """Return a random array of pairs

        Args:
            size (int): Size of the array
            x_values (list): List of values for x
            y_values (list): List of values for y
            pair_distinct (bool, optional): If True, the array will be pair_distinct. Defaults to True.
            order (int, optional): Order of the pair.
                0: non-order
                1: x < y
                2: x <= y
                3: y < x
                4: y <= x

        Returns:
            list: Random array of pairs
        """
        # make all possible pairs
        pairs = []
        for x in x_values:
            for y in y_values:
                pairs.append((x, y))
        # remove pairs that are not order
        if order == 1:
            pairs = [pair for pair in pairs if pair[0] < pair[1]]
        elif order == 2:
            pairs = [pair for pair in pairs if pair[0] <= pair[1]]
        elif order == 3:
            pairs = [pair for pair in pairs if pair[1] < pair[0]]
        elif order == 4:
            pairs = [pair for pair in pairs if pair[1] <= pair[0]]
        # remove pairs that are not pair_distinct
        if pair_distinct:
            pairs = [pair for pair in pairs if pair[0] != pair[1]]
        # return random pairs
        return random.sample(pairs, size)

    def getRandomMatrix(self, rows: int, columns: int, values: list, distinct: bool = False) -> list:
        """Return a random matrix
        Args:
            rows (int): Number of rows
            columns (int): Number of columns
            values (list): List of values
            distinct (bool, optional): If True, the array will be distinct. Defaults to False.
        Returns:
            list: Random matrix
        """
        total = self.getRandomArray(rows * columns, values, distinct=distinct)
        return [total[i * columns: (i + 1) * columns] for i in range(rows)]

    
