import random


class TestCaseGenerator:
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
                pairs.append([x, y])
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

    def getRandomString(self, size: int, chars: str, distinct: bool = False) -> str:
        """Return a random string
        Args:
            size (int): Size of the string
            chars (str): Chars to be used
            distinct (bool, optional): If True, the string will be distinct. Defaults to False.
        Returns:
            str: Random string
        """
        if distinct:
            return ''.join(random.sample(chars, size))
        else:
            return ''.join([random.choice(chars) for _ in range(size)])

    def getRandomCharMatrix(self, rows: int, columns: int, chars: str, distinct: bool = False) -> list:
        """Return a random char matrix
        Args:
            rows (int): Number of rows
            columns (int): Number of columns
            chars (str): Chars to be used
            distinct (bool, optional): If True, the array will be distinct. Defaults to False.
        Returns:
            list: Random char matrix
        """
        total = self.getRandomString(rows * columns, chars, distinct=distinct)
        return [list(total[i * columns: (i + 1) * columns]) for i in range(rows)]

    def getRandomUnweightedTree(self, size: int, start_index: int) -> list:
        """Return a random unweighted tree
        Args:
            size (int): Size of the tree
        Returns:
            list: Random unweighted tree
        """
        edges = []
        for start in range(start_index, start_index + size):
            for end in range(start_index, start_index + size):
                if start != end:
                    cost = self.getRandomNumber(range(int(1e9)))
                    edges.append([start, end, cost])
                    edges.append([end, start, cost])
        return self.Kruskal(edges)

    def Kruskal(self, edges: list) -> list:
        """Return a minimum spanning tree
        Args:
            edges (list): List of edges
        Returns:
            list: Minimum spanning tree
        """
        edges.sort(key=lambda x: x[2])

        parent = [i for i in range(len(edges) + 1)]
        mst = []

        for edge in edges:
            if self.merge(edge[0], edge[1], parent):
                mst.append([edge[0], edge[1]])
        return mst

    def find(self, x: int, parent: list) -> int:
        """Return a parent of x
        Args:
            x (int): Node
            parent (list): Parent list
        Returns:
            int: Parent of x
        """
        if parent[x] == x:
            return x
        else:
            return self.find(parent[x], parent)

    def merge(self, x: int, y: int, parent: list) -> bool:
        """Merge two nodes
        Args:
            x (int): Node
            y (int): Node
            parent (list): Parent list
        Returns:
            bool: If merge is successful
        """
        x = self.find(x, parent)
        y = self.find(y, parent)

        if x < y:
            x, y = y, x

        if x == y:
            return False
        else:
            parent[x] = y
            return True
