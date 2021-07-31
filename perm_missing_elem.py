import unittest
import random

INT_RANGE = (0, 100000)


def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 1

    a_max = max(A)
    sum_ = a_max * (a_max + 1) * 0.5

    missing = int(sum_) - sum(A)

    if missing == 0:
        missing = a_max + 1

    return missing


class TestExercise(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solution([2, 3, 1, 5]), 4)

    def test_single(self):
        self.assertEqual(solution([2]), 1)
        self.assertEqual(solution([1]), 2)
        self.assertEqual(solution([0]), 1)
        self.assertEqual(solution([]), 1)

    def test_random(self):
        arr = [n for n in range(1, random.randint(*INT_RANGE))]
        missing = random.randint(0, len(arr))
        arr.remove(missing)
        self.assertEqual(solution(arr), missing)

    def test_maximum(self):
        arr = [n for n in range(1, INT_RANGE[1] + 1)]
        arr.pop()
        self.assertEqual(solution(arr), INT_RANGE[1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
