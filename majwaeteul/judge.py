from random import randint
from random import sample
from itertools import permutations, combinations


class Problem:
    def __init__(self, problem_number: int):
        self.problem_number = problem_number

    def Run(self):
        # TODO: make Run method
        pass

    def getRandomNumber(self, min_value: int, max_value: int) -> int:
        """임의의 값을 생성합니다.

        Args:
            min_value (int): 값의 최솟값
            max_value (int): 값의 최댓값

        Returns:
            int: 조건을 충족하는 값 중 하나
        """
        assert min_value <= max_value, 'min_value should lower than max_value'
        return randint(min_value, max_value)

    def getRandomArray(self, arr_size: int, min_value: int, max_value: int, is_distinct=False) -> list:
        """임의의 리스트를 생성합니다.

        Args:
            arr_size (int): 리스트의 크기
            min_value (int): 원소의 최솟값
            max_value (int): 원소의 최댓값
            is_distinct (bool, optional): 원소의 유일 여부 (True시 중복 원소가 사라진다). Defaults to False.

        Returns:
            list: 조건을 충족하는 리스트 중 하나
        """
        assert min_value <= max_value, 'min_value should lower than max_value'
        size = max_value - min_value + 1
        assert not is_distinct or is_distinct and arr_size <= size, 'cannot generate distinct array'
        if is_distinct == False:
            return [randint(min_value, max_value) for _ in range(arr_size)]
        # is_distinct == True
        all_combinations = list(map(lambda x: [y for y in x], combinations(
            range(min_value, max_value + 1), arr_size)))
        random_combinations = sample(all_combinations, 1)[0]
        return sample(permutations(random_combinations))[0]

    def getRandomArrayPair(self, arr_pair_size: int, min_first_value: int, max_first_value: int, min_second_value: int, max_second_value: int, is_distinct: bool, pair_type=0) -> list:
        """임의의 쌍들의 리스트를 생성합니다.

        Args:
            arr_pair_size (int): 리스트의 크기
            min_first_value (int): 쌍의 첫번째 원소의 최솟값
            max_first_value (int): 쌍의 첫번째 원소의 최댓값
            min_second_value (int): 쌍의 두번째 원소의 최솟값
            max_second_value (int): 쌍의 두번째 원소의 최솟값
            is_distinct (bool): 쌍의 유일 여부 (True시 중복 쌍이 사라진다)
            pair_type (int, optional): 쌍의 정렬 방식. Defaults to 0.
                0:  랜덤방식으로 쌍을 생성함
                1:  오름차순으로 쌍을 생성함
                2:  비내림차순으로 쌍을 생성함
                3:  내림차순으로 쌍을 생성함
                4:  비내림차순으로 쌍을 생성함

        Returns:
            list: 조건을 만족하는 쌍 리스트 중 하나
        """
        assert min_first_value <= max_first_value, 'min_first_value should lower than max_first_value'
        assert min_second_value <= max_second_value, 'min_second_value should lower than max_second_value'
        assert 0 <= pair_type <= 4, 'pair_type should be in [0, 4] range'

        result = [(i, j) for i in range(min_first_value, max_first_value + 1)
                  for j in range(min_second_value, max_second_value + 1)]
        if pair_type == 1:
            result = list(filter(lambda x: (x[0] < x[1]), result))
        if pair_type == 2:
            result = list(filter(lambda x: (x[0] <= x[1]), result))
        if pair_type == 3:
            result = list(filter(lambda x: (x[0] > x[1]), result))
        if pair_type == 4:
            result = list(filter(lambda x: (x[0] >= x[1]), result))
        size = len(result)
        if is_distinct:
            assert arr_pair_size <= size, 'cannot generate distinct array'
            return sample(result, arr_pair_size)
        # if not is_distint
        return [sample(result, 1)[0] for _ in range(arr_pair_size)]
