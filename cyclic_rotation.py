import unittest
import random

ARRAY_RANGE = (-1000, 1000)
INT_RANGE = (0, 100)


def solution(A, K):
    # write your code in Python 3.6
    new_list = []
    if K > len(A) and len(A) != 0:
        K = K % len(A)
    elif K == len(A) or K == 0:
        return A

    new_list = A[-K:] + A[:-K]

    return new_list


class TestCyclicRotation(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(solution([6, 3, 8, 9, 7], 0), [6, 3, 8, 9, 7])

    def test_one(self):
        self.assertEqual(solution([6, 3, 8, 9, 7], 1), [7, 6, 3, 8, 9])

    def test_example1(self):
        self.assertEqual(solution([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])

    def test_full(self):
        self.assertEqual(solution([6, 3, 8, 9, 7], 5), [6, 3, 8, 9, 7])

    def test_K_bigger_than_A(self):
        self.assertEqual(solution([1, 1, 2, 3, 5], 42), [3, 5, 1, 1, 2])

    def test_empty(self):
        self.assertEqual(solution([], 5), [])

    def test_random(self):
        N = random.randint(*INT_RANGE)
        K = random.randint(*INT_RANGE)
        A = [random.randint(*ARRAY_RANGE) for i in range(0, N)]


if __name__ == "__main__":
    unittest.main(verbosity=2)
