from main import sum_of_two
import unittest

class TestSumOfTwo(unittest.TestCase):

    def test_two_res(self):
        self.assertEqual(sum_of_two([2, 7, 11, 15,9,0], 9), [[0, 1],[4,5]])

    def test_only_one_res(self):
        self.assertEqual(sum_of_two([3, 3], 6), [[0, 1]])

    def test_not_res(self):
        self.assertEqual(sum_of_two([3, 4], 6), [])

    def test_not_mas(self):
        with self.assertRaises(TypeError):
            sum_of_two([], 2)

    def test_target_str(self):
        with self.assertRaises(TypeError):
            sum_of_two([1, 2, 3], "6")

    def test_nums_int(self):
        with self.assertRaises(TypeError):
            sum_of_two(1, 6)


if __name__ == '__main__':
    unittest.main()
